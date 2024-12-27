import streamlit as st
import fitz  # PyMuPDF
import os
import face_recognition
import numpy as np
from PIL import Image
import io
import cv2
import pytesseract
from pdf2image import convert_from_bytes

# Configure page settings
st.set_page_config(
    page_title="PDF Face Detection & OCR",
    page_icon="👤",
    layout="wide"
)

# Add title and description
st.title("PDF Face Detection & OCR App")
st.write("Upload a PDF to detect faces and perform text redaction (works with both text and image-based PDFs)")

def perform_ocr_on_page(image):
    """Perform OCR on an image and return the text"""
    try:
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        st.error(f"OCR Error: {str(e)}")
        return ""

def create_searchable_pdf(pdf_file):
    """Convert image-based PDF to searchable PDF"""
    try:
        # Convert PDF to images
        pdf_bytes = io.BytesIO(pdf_file.getvalue())
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
            
            # Insert image
            page.insert_image(page.rect, stream=img_bytes)
            
            # Perform OCR
            text = perform_ocr_on_page(img)
            
            # Insert text layer
            if text:
                page.insert_text((0, 0), text)
        
        # Convert to bytes
        output_bytes = io.BytesIO()
        output_pdf.save(output_bytes)
        output_pdf.close()
        
        return output_bytes.getvalue()
    except Exception as e:
        st.error(f"Error creating searchable PDF: {str(e)}")
        return None

def process_pdf_faces(pdf_file):
    results = []
    pdf_document = None
    try:
        # Create searchable PDF if needed
        pdf_bytes = io.BytesIO(pdf_file.getvalue())
        pdf_document = fitz.open(stream=pdf_bytes)
        
        # Check if PDF needs OCR (by checking if it has text)
        needs_ocr = True
        for page in pdf_document:
            if page.get_text().strip():
                needs_ocr = False
                break
        
        if needs_ocr:
            st.info("Converting image-based PDF to searchable format...")
            searchable_pdf = create_searchable_pdf(pdf_file)
            if searchable_pdf:
                pdf_document = fitz.open(stream=io.BytesIO(searchable_pdf))
        
        total_pages = len(pdf_document)
        
        for page_num in range(total_pages):
            page = pdf_document[page_num]
            
            # Convert PDF page to image
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            
            # Convert PIL image to numpy array
            img_array = np.array(img)
            
            # Detect faces
            face_locations = face_recognition.face_locations(img_array)
            
            # Store results
            page_results = {
                'page_number': page_num + 1,
                'face_count': len(face_locations),
                'faces': []
            }
            
            for face_location in face_locations:
                top, right, bottom, left = face_location
                face_info = {
                    'top': top / pix.height,
                    'right': right / pix.width,
                    'bottom': bottom / pix.height,
                    'left': left / pix.width
                }
                page_results['faces'].append(face_info)
            
            results.append(page_results)
        
        return {
            'status': 'success',
            'total_pages': total_pages,
            'pages': results
        }
        
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }
    finally:
        if pdf_document:
            pdf_document.close()

def mask_faces_on_page(pdf_file, page_num, faces):
    try:
        # Create a bytes buffer
        pdf_bytes = io.BytesIO(pdf_file.getvalue())
        
        # Open PDF and get specified page
        pdf_document = fitz.open(stream=pdf_bytes)
        page = pdf_document[page_num]
        
        # Convert page to image
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img_array = np.array(img)
        
        # Mask each face with a black rectangle
        for face in faces:
            top = int(face['top'] * pix.height)
            right = int(face['right'] * pix.width)
            bottom = int(face['bottom'] * pix.height)
            left = int(face['left'] * pix.width)
            
            # Draw black rectangle over face
            img_array[top:bottom, left:right] = [0, 0, 0]  # Black mask
        
        # Convert back to PIL Image and then to bytes
        result_img = Image.fromarray(img_array)
        img_byte_arr = io.BytesIO()
        result_img.save(img_byte_arr, format='PNG')
        img_bytes = img_byte_arr.getvalue()
        
        pdf_document.close()
        return img_bytes
        
    except Exception as e:
        st.error(f"Error masking faces: {str(e)}")
        return None

def redact_text_on_page(pdf_file, page_num, text_patterns):
    try:
        # Create a bytes buffer
        pdf_bytes = io.BytesIO(pdf_file.getvalue())
        
        # Open PDF and get specified page
        pdf_document = fitz.open(stream=pdf_bytes)
        page = pdf_document[page_num]
        
        # Split patterns and clean them
        patterns = [p.strip() for p in text_patterns.split(',') if p.strip()]
        
        # Search and redact each pattern
        for pattern in patterns:
            text_instances = page.search_for(pattern)
            for inst in text_instances:
                # Draw black rectangle over the text
                page.draw_rect(inst, color=(0, 0, 0), fill=(0, 0, 0))
        
        # Convert to image
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
        img_bytes = pix.tobytes("png")
        
        pdf_document.close()
        return img_bytes, len(text_instances) if text_instances else 0
        
    except Exception as e:
        st.error(f"Error redacting text: {str(e)}")
        return None, 0

# File uploader
uploaded_file = st.file_uploader("Choose a PDF file", type=['pdf'])

if uploaded_file is not None:
    # Initialize session state for PDF content
    if 'pdf_content' not in st.session_state:
        st.session_state.pdf_content = uploaded_file.getvalue()
    
    # Add text input for redaction patterns
    text_to_redact = st.text_input(
        "Enter text patterns to redact (comma-separated)",
        help="Example: John Doe, 123-45-6789, confidential"
    )
    
    # Create columns for layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### PDF Preview")
        try:
            pdf_bytes = io.BytesIO(st.session_state.pdf_content)
            pdf_document = fitz.open(stream=pdf_bytes)
            first_page = pdf_document[0]
            pix = first_page.get_pixmap(matrix=fitz.Matrix(1, 1))
            img_bytes = pix.tobytes("png")
            pdf_document.close()
            st.image(img_bytes)
        except Exception as e:
            st.error(f"Error displaying preview: {str(e)}")
    
    with col2:
        st.write("### Detection Results")
        if st.button("Process PDF (Mask Faces & Redact Text)"):
            with st.spinner("Processing PDF..."):
                # First check if PDF needs OCR
                pdf_bytes = io.BytesIO(uploaded_file.getvalue())
                pdf_document = fitz.open(stream=pdf_bytes)
                
                needs_ocr = True
                for page in pdf_document:
                    if page.get_text().strip():
                        needs_ocr = False
                        break
                pdf_document.close()
                
                if needs_ocr:
                    st.info("Converting image-based PDF to searchable format...")
                    searchable_pdf = create_searchable_pdf(uploaded_file)
                    if searchable_pdf:
                        uploaded_file = io.BytesIO(searchable_pdf)
                        st.session_state.pdf_content = searchable_pdf
                
                # Process faces and text
                results = process_pdf_faces(uploaded_file)
                
                if results['status'] == 'success':
                    total_faces = sum(page['face_count'] for page in results['pages'])
                    st.success(f"Found {total_faces} faces across {results['total_pages']} pages")
                    
                    for page in results['pages']:
                        with st.expander(f"Page {page['page_number']}"):
                            processed_img = None
                            
                            # First mask faces if any found
                            if page['face_count'] > 0:
                                processed_img = mask_faces_on_page(
                                    uploaded_file,
                                    page['page_number'] - 1,
                                    page['faces']
                                )
                                st.info(f"Masked {page['face_count']} faces on this page")
                            
                            # Then apply text redaction if patterns provided
                            if text_to_redact:
                                img_bytes, redaction_count = redact_text_on_page(
                                    uploaded_file if processed_img is None else io.BytesIO(processed_img),
                                    page['page_number'] - 1,
                                    text_to_redact
                                )
                                if redaction_count > 0:
                                    st.info(f"Redacted {redaction_count} text instances on this page")
                                    processed_img = img_bytes
                            
                            # Display the processed page
                            if processed_img:
                                st.image(processed_img)
                            else:
                                # If no processing was needed, show original page
                                pdf_bytes = io.BytesIO(uploaded_file.getvalue())
                                pdf_document = fitz.open(stream=pdf_bytes)
                                page_obj = pdf_document[page['page_number'] - 1]
                                pix = page_obj.get_pixmap(matrix=fitz.Matrix(2, 2))
                                st.image(pix.tobytes("png"))
                                pdf_document.close()
                else:
                    st.error(f"Error processing PDF: {results['message']}")

# Add footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")