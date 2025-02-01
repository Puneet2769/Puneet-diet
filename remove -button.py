import os

# Directory containing your HTML files
directory = 'C:/Users/punee/Desktop/coding/Website'

# Define the unique HTML patterns for each type of button
extra_button_1 = '<button class="back-button">Back</button>'
extra_button_2 = '<button onclick="window.history.back()">Back</button>'

# Loop through all HTML files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        file_path = os.path.join(directory, filename)
        
        # Read the existing content
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Remove extra buttons while keeping the correct one
        content = content.replace(extra_button_1, '')
        content = content.replace(extra_button_2, '')
        
        # Ensure one button with class `back-button` remains
        if '<button class="back-button" onclick="window.history.back()">Back</button>' not in content:
            content = content.replace('</body>', '<button class="back-button" onclick="window.history.back()">Back</button>\n</body>')
        
        # Write the modified content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        
        print(f"Updated {filename}")
