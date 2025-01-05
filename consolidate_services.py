import os
import shutil
import glob
from pathlib import Path
from datetime import datetime

def ensure_directory(path):
    """Create directory if it doesn't exist."""
    Path(path).mkdir(parents=True, exist_ok=True)

def move_files(src_dir, dest_dir, pattern="*"):
    """Move files matching pattern from src to dest directory."""
    if not os.path.exists(src_dir):
        print(f"Source directory {src_dir} does not exist.")
        return

    ensure_directory(dest_dir)
    
    for filepath in glob.glob(os.path.join(src_dir, pattern)):
        if os.path.isfile(filepath):
            filename = os.path.basename(filepath)
            dest_path = os.path.join(dest_dir, filename)
            
            if os.path.exists(dest_path):
                # Keep newer file
                src_time = os.path.getmtime(filepath)
                dest_time = os.path.getmtime(dest_path)
                if src_time <= dest_time:
                    print(f"Skipping {filename} - newer version exists")
                    continue
            
            print(f"Moving {filename} to {dest_dir}")
            shutil.move(filepath, dest_path)

def merge_requirements(src_file, dest_file):
    """Merge requirements files, keeping unique entries."""
    if not os.path.exists(src_file):
        return
    
    requirements = set()
    
    # Read existing requirements if any
    if os.path.exists(dest_file):
        with open(dest_file, 'r') as f:
            requirements.update(line.strip() for line in f if line.strip())
    
    # Add new requirements
    with open(src_file, 'r') as f:
        requirements.update(line.strip() for line in f if line.strip())
    
    # Write merged requirements
    with open(dest_file, 'w') as f:
        for req in sorted(requirements):
            f.write(req + '\n')

def update_imports(src_dir):
    """Update import statements in Python files."""
    for filepath in glob.glob(os.path.join(src_dir, "**/*.py"), recursive=True):
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Update relative imports
        content = content.replace('from services.', 'from ')
        content = content.replace('import services.', 'import ')
        
        with open(filepath, 'w') as f:
            f.write(content)

def main():
    # Service directories mapping
    services = {
        'face-detection': 'face_detection',
        'guardian-analyzer': 'guardian_analyzer',
        'presidio': 'presidio'
    }

    # Process each service
    for old_name, new_name in services.items():
        src_dir = os.path.join('services', old_name)
        dest_dir = os.path.join(new_name, 'src')
        
        print(f"\nProcessing {old_name}...")
        
        # Move Python files
        move_files(src_dir, dest_dir, "*.py")
        
        # Move other files (configs, etc)
        move_files(src_dir, dest_dir)
        
        # Merge requirements
        src_req = os.path.join(src_dir, 'requirements.txt')
        dest_req = os.path.join(new_name, 'requirements.txt')
        merge_requirements(src_req, dest_req)
        
        # Update import paths
        update_imports(dest_dir)

    # Remove old services directory if empty
    if os.path.exists('services'):
        try:
            shutil.rmtree('services')
            print("\nRemoved old services directory")
        except OSError as e:
            print(f"\nWarning: Could not remove services directory: {e}")

if __name__ == "__main__":
    main()

