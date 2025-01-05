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

## License

This project is licensed under the MIT License - see the LICENSE file for details.
