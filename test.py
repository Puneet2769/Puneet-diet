import os

# Directory containing your HTML files
directory = 'C:/Users/punee/Desktop/coding/Website'

# HTML content to be added
back_button_html = '''
   <button onclick="window.history.back()">Back</button>
'''

# Loop through all HTML files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        file_path = os.path.join(directory, filename)
        # Read the existing content
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Check if the button is already present
        if back_button_html.strip() not in content:
            # Add the button before the closing </body> tag
            content = content.replace('</body>', f'{back_button_html}\n</body>')
            
            # Write the modified content back to the file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            
            print(f"Updated {filename}")
        else:
            print(f"Back button already present in {filename}")
