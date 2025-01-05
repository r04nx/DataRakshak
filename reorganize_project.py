import fnmatch
#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

def create_directory_structure():
    """Create the main directory structure for the project."""
    directories = [
        'face_detection',
        'guardian_analyzer',
        'presidio',
        'shared',
        'data',
        'docs',
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        os.makedirs(f"{directory}/src", exist_ok=True)
        
    # Create data subdirectories
    data_dirs = ['raw', 'processed', 'models']
    for data_dir in data_dirs:
        os.makedirs(f"data/{data_dir}", exist_ok=True)

def create_requirements():
    """Create requirements files for each service and main project."""
    # Main requirements
    main_requirements = [
        'numpy',
        'opencv-python',
        'pillow',
        'tqdm',
        'requests',
        'python-dotenv'
    ]
    
    # Service-specific requirements
    service_requirements = {
        'face_detection': [
            'opencv-python',
            'numpy',
            'pillow',
            'tqdm'
        ],
        'guardian_analyzer': [
            'requests',
            'python-dotenv',
            'pandas'
        ],
        'presidio': [
            'presidio-analyzer',
            'presidio-anonymizer'
        ]
    }
    
    # Write main requirements
    with open('requirements.txt', 'w') as f:
        f.write('\n'.join(main_requirements))
    
    # Write service requirements
    for service, reqs in service_requirements.items():
        with open(f"{service}/requirements.txt", 'w') as f:
            f.write('\n'.join(reqs))

def create_readme():
    """Create a comprehensive README.md file."""
    readme_content = """# Obsidian Project

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
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
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
"""
    
    with open('README.md', 'w') as f:
        f.write(readme_content)

def create_gitignore():
    """Create a comprehensive .gitignore file."""
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual Environment
venv/
ENV/
env/
.env

# IDEs
.idea/
.vscode/
*.swp
*.swo
*~

# Project specific
data/raw/*
data/processed/*
!data/raw/.gitkeep
!data/processed/.gitkeep
*.log
.DS_Store
"""
    
    with open('.gitignore', 'w') as f:
        f.write(gitignore_content)

def organize_files():
    """Move existing files to their appropriate directories."""
    # Service-specific file patterns
    service_patterns = {
        'face_detection': {
            'files': ['face_*.py', '*_face*.py', 'detect_*.py'],
            'extensions': ['.py'],
            'keywords': ['face', 'detection', 'opencv']
        },
        'guardian_analyzer': {
            'files': ['analyze_*.py', 'guardian_*.py', 'content_*.py'],
            'extensions': ['.py'],
            'keywords': ['analyze', 'guardian', 'content']
        },
        'presidio': {
            'files': ['pii_*.py', 'privacy_*.py', 'anonymize_*.py'],
            'extensions': ['.py'],
            'keywords': ['pii', 'privacy', 'anonymize']
        },
        'shared': {
            'files': ['utils.py', 'common.py', 'config.py'],
            'extensions': ['.py'],
            'keywords': ['util', 'common', 'shared', 'config']
        }
    }

    # Data file extensions
    data_extensions = {
        'images': {'.jpg', '.jpeg', '.png', '.gif'},
        'videos': {'.mp4', '.avi', '.mov'},
        'audio': {'.wav', '.mp3', '.ogg'},
        'models': {'.h5', '.pkl', '.model'}
    }

    # Create .gitkeep files in empty directories
    for root, dirs, files in os.walk('.'):
        if not files and not dirs:
            Path(os.path.join(root, '.gitkeep')).touch()

    # Process files in current directory
    for item in os.listdir('.'):
        if not os.path.isfile(item):
            continue

        try:
            # Skip common system files and current script
            if item.startswith('.') or item == os.path.basename(__file__):
                continue

            # Check for service-specific files
            for service, patterns in service_patterns.items():
                if any(fnmatch.fnmatch(item.lower(), pattern.lower()) for pattern in patterns['files']) or \
                any(item.lower().endswith(ext.lower()) for ext in patterns['extensions']) and \
                any(keyword in item.lower() for keyword in patterns['keywords']):
                    dest_dir = f"{service}/src"
                    print(f"Moving {item} to {dest_dir}")
                    shutil.move(item, os.path.join(dest_dir, item))
                    break

            # Check for data files
            name, ext = os.path.splitext(item.lower())
            for data_type, extensions in data_extensions.items():
                if ext in extensions:
                    if data_type == 'models':
                        dest_dir = "data/models"
                    else:
                        dest_dir = "data/raw"
                    print(f"Moving data file {item} to {dest_dir}")
                    shutil.move(item, os.path.join(dest_dir, item))
                    break

        except (shutil.Error, OSError) as e:
            print(f"Error moving {item}: {str(e)}")

def main():
    """Main function to organize the project."""
    print("Starting project reorganization...")
    
    # Create main structure
    create_directory_structure()
    print("✓ Created directory structure")
    
    # Create requirement files
    create_requirements()
    print("✓ Created requirements files")
    
    # Create README
    create_readme()
    print("✓ Created README.md")
    
    # Create gitignore
    create_gitignore()
    print("✓ Created .gitignore")
    
    # Organize existing files
    organize_files()
    print("✓ Organized existing files")
    
    print("\nProject reorganization complete!")
    print("Please review the changes and update any file paths in your code.")

if __name__ == "__main__":
    main()

