# Data Rakshak

A hackathon project for processing and analyzing media content with face detection and privacy features.

## Project Structure

```
.
├── face_detection/      # Face detection and processing service
├── guardian_analyzer/   # Content analysis service
├── presidio/           # Privacy and PII detection service
├── shared/             # Shared utilities and common code
├── data/               # Data storage
│   ├── raw/            # Raw input data
│   ├── processed/      # Processed output data
│   └── models/         # Model files and weights
└── docs/               # Documentation

```

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/r04nx/Obsidian.git
cd Obsidian
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install service-specific dependencies:
```bash
pip install -r face_detection/requirements.txt
pip install -r guardian_analyzer/requirements.txt
pip install -r presidio/requirements.txt
```

## Services

### Face Detection
- Processes images and videos to detect and extract faces
- Supports batch processing and real-time detection
- Includes face quality assessment and filtering

### Guardian Analyzer
- Analyzes content for sensitive information
- Integrates with external APIs for content verification
- Provides content classification and filtering

### Presidio Integration
- Detects and anonymizes PII (Personally Identifiable Information)
- Supports multiple languages and entity types
- Configurable anonymization patterns

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

# DataRakshak

A comprehensive data protection and privacy solution developed for a hackathon. This project focuses on identifying and securing sensitive information across various data formats.

## Features

- Privacy-preserving data analysis
- Sensitive information detection
- Data redaction and anonymization
- Support for multiple document formats
- Face detection and privacy protection
- Guardian analyzer for enhanced security

## Project Structure

- `/services`
  - `face-detection/`: Face detection and privacy protection service
  - `guardian-analyzer/`: Advanced data analysis and protection
  - `presidio/`: Core privacy engine implementation
- `/backend`: Backend API and database management
- `/frontend`: React-based web interface

## Setup

1. Install dependencies:
   ```bash
   npm install # For frontend
   pip install -r requirements.txt # For Python services
   ```

2. Run the development server:
   ```bash
   npm run dev # Frontend
   python main.py # Backend
   ```

## License

MIT License

