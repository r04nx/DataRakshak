from flask import Flask, request, send_file
from flask_restx import Api, Resource, fields
import fitz
import face_recognition
import numpy as np
from PIL import Image, ImageFilter
import io
import pytesseract
from pdf2image import convert_from_bytes
from werkzeug.datastructures import FileStorage

app = Flask(__name__)
api = Api(app, version='1.0', title='PDF Face Detection & OCR API',
          description='API for PDF processing with face detection and text redaction')

# Define namespaces
pdf_ns = api.namespace('pdf', description='PDF processing operations')

# Define models for documentation
process_response = api.model('ProcessResponse', {
    'status': fields.String(required=True, description='Processing status'),
    'total_pages': fields.Integer(description='Total number of pages'),
    'pages': fields.List(fields.Raw, description='Page-wise results')
})

# Define file upload parser
upload_parser = api.parser()
upload_parser.add_argument('file', location='files', type=FileStorage, required=True)
upload_parser.add_argument('text_patterns', type=str, help='Comma-separated text patterns to redact')

# Reuse your existing helper functions
def perform_ocr_on_page(image):
    """Perform OCR on an image and return the text"""
    try:
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        return ""

def create_searchable_pdf(pdf_file):
    """Convert image-based PDF to searchable PDF"""
    try:
        # Convert PDF to images
        pdf_bytes = io.BytesIO(pdf_file.read())
        images = convert_from_bytes(pdf_bytes.getvalue())
        
        # Create new PDF
        output_pdf = fitz.open()
        
        for img in images:
            # Convert PIL image to bytes
            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format='PNG')
            img_bytes = img_byte_arr.getvalue()
            
            # Create new PDF page
            page = output_pdf.new_page(width=img.width, height=img.height)
            
            # Insert image and OCR text
            page.insert_image(page.rect, stream=img_bytes)
            text = perform_ocr_on_page(img)
            if text:
                page.insert_text((0, 0), text)
        
        # Convert to bytes
        output_bytes = io.BytesIO()
        output_pdf.save(output_bytes)
        output_pdf.close()
        
        return output_bytes.getvalue()
    except Exception as e:
        return None

def process_pdf_faces(pdf_file):
    """Process PDF file for face detection"""
    try:
        pdf_bytes = io.BytesIO(pdf_file.read())
        pdf_document = fitz.open(stream=pdf_bytes)
        results = {
            'status': 'success',
            'total_pages': len(pdf_document),
            'pages': []
        }

        for page_num in range(len(pdf_document)):
            page = pdf_document[page_num]
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            
            # Convert PIL Image to numpy array for face_recognition
            img_np = np.array(img)
            
            # Detect faces
            face_locations = face_recognition.face_locations(img_np)
            
            # Store results
            page_results = {
                'page_number': page_num + 1,
                'faces_found': len(face_locations),
                'face_locations': face_locations
            }
            results['pages'].append(page_results)

        pdf_document.close()
        return results

    except Exception as e:
        return {'status': 'error', 'message': str(e)}

def redact_text_on_page(pdf_file, page_num, text_patterns):
    """Redact specified text patterns on a page"""
    try:
        pdf_document = fitz.open(stream=pdf_file)
        page = pdf_document[page_num]
        redaction_count = 0
        
        # Split patterns if provided as comma-separated string
        if isinstance(text_patterns, str):
            patterns = [p.strip() for p in text_patterns.split(',')]
        else:
            patterns = text_patterns

        for pattern in patterns:
            instances = page.search_for(pattern)
            redaction_count += len(instances)
            [page.add_redact_annot(inst, fill=(0, 0, 0)) for inst in instances]
        
        page.apply_redactions()
        return pdf_document, redaction_count

    except Exception as e:
        return None, 0

def mask_faces_on_page(img_np, face_locations, blur=True):
    """Mask detected faces in an image either by blurring or black rectangle"""
    img = Image.fromarray(img_np)
    
    for (top, right, bottom, left) in face_locations:
        face_region = img.crop((left, top, right, bottom))
        
        if blur:
            # Apply Gaussian blur
            face_region = face_region.filter(ImageFilter.GaussianBlur(radius=15))
        else:
            # Create black rectangle
            face_region = Image.new('RGB', (right-left, bottom-top), 'black')
        
        img.paste(face_region, (left, top, right, bottom))
    
    return img

@pdf_ns.route('/process')
class ProcessPDF(Resource):
    @pdf_ns.expect(upload_parser)
    @pdf_ns.response(200, 'Success', process_response)
    @pdf_ns.response(400, 'Bad Request')
    def post(self):
        """Process PDF file for face detection and text redaction"""
        try:
            args = upload_parser.parse_args()
            pdf_file = args['file']
            text_patterns = args.get('text_patterns', '')

            if not pdf_file:
                return {'status': 'error', 'message': 'No file provided'}, 400

            print(f"Processing file: {pdf_file.filename}")  # Debug print
            
            # Check if PDF needs OCR
            pdf_bytes = io.BytesIO(pdf_file.read())
            pdf_document = fitz.open(stream=pdf_bytes)
            
            needs_ocr = True
            for page in pdf_document:
                if page.get_text().strip():
                    needs_ocr = False
                    break
            pdf_document.close()
            
            # Reset file pointer
            pdf_file.seek(0)
            
            if needs_ocr:
                searchable_pdf = create_searchable_pdf(pdf_file)
                if searchable_pdf:
                    pdf_file = io.BytesIO(searchable_pdf)

            # Process faces and text
            results = process_pdf_faces(pdf_file)
            
            if results['status'] == 'success' and text_patterns:
                # Apply text redaction if patterns provided
                pdf_bytes = io.BytesIO(pdf_file.read())
                pdf_document = fitz.open(stream=pdf_bytes)
                
                for page_num in range(len(pdf_document)):
                    _, redaction_count = redact_text_on_page(
                        pdf_file,
                        page_num,
                        text_patterns
                    )
                    if redaction_count > 0:
                        results['pages'][page_num]['redacted_text_count'] = redaction_count
                
                pdf_document.close()

            return results

        except Exception as e:
            print(f"Error processing request: {str(e)}")  # Debug print
            return {'status': 'error', 'message': str(e)}, 400

@pdf_ns.route('/download/<int:page_num>')
class DownloadProcessedPage(Resource):
    @pdf_ns.doc(params={'page_num': 'Page number to download'})
    @pdf_ns.response(200, 'Success')
    @pdf_ns.response(400, 'Bad Request')
    def get(self, page_num):
        """Download a processed page as an image"""
        try:
            # Implementation for downloading processed pages
            # You'll need to implement session handling or temporary storage
            # for processed files
            pass
        except Exception as e:
            return {'status': 'error', 'message': str(e)}, 400

@pdf_ns.route('/redact-faces')
class RedactFacesPDF(Resource):
    @pdf_ns.expect(upload_parser)
    @pdf_ns.response(200, 'Success')
    @pdf_ns.response(400, 'Bad Request')
    def post(self):
        """Process PDF file to detect and redact faces"""
        try:
            args = upload_parser.parse_args()
            pdf_file = args['file']

            if not pdf_file:
                return {'status': 'error', 'message': 'No file provided'}, 400

            print(f"Processing file: {pdf_file.filename}")
            
            # Read PDF
            pdf_bytes = io.BytesIO(pdf_file.read())
            pdf_document = fitz.open(stream=pdf_bytes)
            output_pdf = fitz.open()  # New PDF for output
            
            results = {
                'status': 'success',
                'total_pages': len(pdf_document),
                'pages': []
            }

            for page_num in range(len(pdf_document)):
                page = pdf_document[page_num]
                pix = page.get_pixmap()
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                
                # Convert to numpy array for face detection
                img_np = np.array(img)
                
                # Detect faces
                face_locations = face_recognition.face_locations(img_np)
                
                if face_locations:
                    # Mask faces if found
                    masked_img = mask_faces_on_page(img_np, face_locations, blur=True)
                    
                    # Create new PDF page
                    new_page = output_pdf.new_page(width=page.rect.width, 
                                                 height=page.rect.height)
                    
                    # Convert masked image to bytes
                    img_byte_arr = io.BytesIO()
                    masked_img.save(img_byte_arr, format='PNG')
                    img_bytes = img_byte_arr.getvalue()
                    
                    # Insert masked image
                    new_page.insert_image(new_page.rect, stream=img_bytes)
                else:
                    # If no faces found, copy original page
                    output_pdf.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)
                
                # Store results
                page_results = {
                    'page_number': page_num + 1,
                    'faces_found': len(face_locations),
                    'face_locations': face_locations
                }
                results['pages'].append(page_results)

            # Save processed PDF to bytes
            output_bytes = io.BytesIO()
            output_pdf.save(output_bytes)
            output_pdf.close()
            pdf_document.close()
            
            # Return processed PDF
            output_bytes.seek(0)
            return send_file(
                output_bytes,
                mimetype='application/pdf',
                as_attachment=True,
                download_name='redacted_faces.pdf'
            )

        except Exception as e:
            print(f"Error processing request: {str(e)}")
            return {'status': 'error', 'message': str(e)}, 400

if __name__ == '__main__':
    app.run(debug=True)