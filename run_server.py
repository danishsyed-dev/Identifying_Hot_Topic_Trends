#!/usr/bin/env python
"""Script to run Django server - handles special character paths"""
import os
import sys
import importlib.util

# Get the absolute path to THIS script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Add to Python path
sys.path.insert(0, script_dir)

# Change working directory
os.chdir(script_dir)

# Configure Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'identifying_hot_topic_trends.settings'

# Force Python to recognize the package
package_path = os.path.join(script_dir, 'identifying_hot_topic_trends')

if os.path.isdir(package_path) and 'identifying_hot_topic_trends' not in sys.modules:
    # Create a module spec and load the package
    init_file = os.path.join(package_path, '__init__.py')
    spec = importlib.util.spec_from_file_location(
        'identifying_hot_topic_trends',
        init_file,
        submodule_search_locations=[package_path]
    )
    if spec and spec.loader:
        module = importlib.util.module_from_spec(spec)
        sys.modules['identifying_hot_topic_trends'] = module
        spec.loader.exec_module(module)
        print("✓ Package loaded")

# Now load settings
if 'identifying_hot_topic_trends.settings' not in sys.modules:
    settings_path = os.path.join(package_path, 'settings.py')
    spec = importlib.util.spec_from_file_location('identifying_hot_topic_trends.settings', settings_path)
    if spec and spec.loader:
        settings_module = importlib.util.module_from_spec(spec)
        sys.modules['identifying_hot_topic_trends.settings'] = settings_module
        spec.loader.exec_module(settings_module)
        print("✓ Settings loaded")

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    print("\n✓ Starting Django server...")
    print("Open http://127.0.0.1:8000/ in your browser\n")
    execute_from_command_line(['manage.py', 'runserver', '127.0.0.1:8000'])
