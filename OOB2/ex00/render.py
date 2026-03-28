import sys
import os
import re

def render():
    # Check number of arguments
    if len(sys.argv) != 2:
        print("Error: Wrong number of arguments.")
        return

    template_file = sys.argv[1]

    # Check file extension
    if not template_file.endswith(".template"):
        print("Error: The file must have a .template extension.")
        return

    # Check if file exists
    if not os.path.exists(template_file):
        print(f"Error: The file '{template_file}' does not exist.")
        return

    try:
        # Load settings.py manually to avoid import path issues
        settings_vars = {}
        if not os.path.exists("settings.py"):
            print("Error: settings.py not found.")
            return
            
        with open("settings.py", "r", encoding="utf-8") as f:
            exec(f.read(), {}, settings_vars)

        # Read the template file
        with open(template_file, 'r', encoding="utf-8") as f:
            content = f.read()

        # Output file name: replace .template with .html
        output_file = template_file.replace(".template", ".html")

        # Perform replacement using format and the settings dictionary
        # This is what "keyword expansion" refers to: **settings_vars
        try:
            output_content = content.format(**settings_vars)
        except KeyError as e:
            print(f"Error: Variable {e} not found in settings.py")
            return

        # Write to the .html file
        with open(output_file, 'w', encoding="utf-8") as f:
            f.write(output_content)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    render()
