#!/usr/bin/env python
"""
Setup Validation Script for Identifying Hot Topic Trends
This script checks if the project is properly set up and ready to run.
"""

import sys
import os

def print_status(message, status):
    """Print colored status message"""
    if status:
        print(f"✓ {message}")
    else:
        print(f"✗ {message}")
    return status

def check_python_version():
    """Check if Python version is 3.10 or higher"""
    version = sys.version_info
    is_valid = version.major == 3 and version.minor >= 10
    print_status(f"Python version {version.major}.{version.minor}.{version.micro}", is_valid)
    if not is_valid:
        print("  Error: Python 3.10 or higher is required")
    return is_valid

def check_django():
    """Check if Django is installed"""
    try:
        import django
        print_status(f"Django installed (version {django.get_version()})", True)
        return True
    except ImportError:
        print_status("Django installed", False)
        print("  Run: pip install -r requirements.txt")
        return False

def check_dependencies():
    """Check if all required dependencies are installed"""
    dependencies = {
        'sklearn': 'scikit-learn',
        'gensim': 'gensim',
        'numpy': 'numpy',
        'pandas': 'pandas',
        'openpyxl': 'openpyxl',
        'xlwt': 'xlwt'
    }
    
    all_installed = True
    for module, package in dependencies.items():
        try:
            __import__(module)
            print_status(f"{package} installed", True)
        except ImportError:
            print_status(f"{package} installed", False)
            all_installed = False
    
    if not all_installed:
        print("\n  Run: pip install -r requirements.txt")
    return all_installed

def check_dataset():
    """Check if Datasets.csv exists"""
    exists = os.path.exists('Datasets.csv')
    print_status("Datasets.csv exists", exists)
    if not exists:
        print("  Error: Sample dataset not found. Please ensure Datasets.csv is in the root directory.")
    else:
        # Try to load and validate the dataset
        try:
            import pandas as pd
            data = pd.read_csv('Datasets.csv', encoding='latin-1')
            has_columns = 'Description' in data.columns and 'Label' in data.columns
            print_status(f"Dataset has correct structure ({len(data)} samples)", has_columns)
            if has_columns:
                label_counts = data['Label'].value_counts()
                print(f"    - Hot Topics (1): {label_counts.get(1, 0)}")
                print(f"    - Normal Topics (0): {label_counts.get(0, 0)}")
            return has_columns
        except Exception as e:
            print_status("Dataset readable", False)
            print(f"  Error: {str(e)}")
            return False
    return exists

def check_database():
    """Check if database is set up"""
    exists = os.path.exists('db.sqlite3')
    print_status("Database file exists", exists)
    if not exists:
        print("  Run: python manage.py migrate")
    return exists

def check_project_structure():
    """Check if key project directories exist"""
    required_dirs = [
        'identifying_hot_topic_trends',
        'Remote_User',
        'Service_Provider',
        'Template'
    ]
    
    all_exist = True
    for directory in required_dirs:
        exists = os.path.isdir(directory)
        if not exists:
            print_status(f"Directory '{directory}' exists", False)
            all_exist = False
    
    if all_exist:
        print_status("Project structure is complete", True)
    return all_exist

def main():
    """Run all checks"""
    print("=" * 60)
    print("Identifying Hot Topic Trends - Setup Validation")
    print("=" * 60)
    print()
    
    checks = [
        ("Python Version", check_python_version),
        ("Django Installation", check_django),
        ("Dependencies", check_dependencies),
        ("Dataset", check_dataset),
        ("Database", check_database),
        ("Project Structure", check_project_structure),
    ]
    
    results = []
    for check_name, check_func in checks:
        print(f"\n{check_name}:")
        print("-" * 40)
        result = check_func()
        results.append(result)
    
    print("\n" + "=" * 60)
    if all(results):
        print("✓ All checks passed! The project is ready to run.")
        print("\nTo start the server, run:")
        print("  python manage.py runserver")
        return 0
    else:
        print("✗ Some checks failed. Please fix the issues above.")
        print("\nQuick fix:")
        print("  pip install -r requirements.txt")
        print("  python manage.py migrate")
        return 1
    
if __name__ == "__main__":
    sys.exit(main())
