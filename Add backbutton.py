# import os

# # Directory containing your HTML files
# directory = 'C:/Users/punee/Desktop/coding/Website'

# # HTML content to be removed
# old_back_button_html = '<button onclick="window.history.back()">Back</button>'

# # Loop through all HTML files in the directory
# for filename in os.listdir(directory):
#     if filename.endswith(".html"):
#         file_path = os.path.join(directory, filename)
        
#         # Read the existing content
#         with open(file_path, 'r', encoding='utf-8') as file:
#             content = file.read()
        
#         # Remove the old back button HTML content
#         if old_back_button_html in content:
#             content = content.replace(old_back_button_html, '')
            
#             # Write the modified content back to the file
#             with open(file_path, 'w', encoding='utf-8') as file:
#                 file.write(content)
            
#             print(f"Removed old back button from {filename}")
#         else:
#             print(f"No old back button found in {filename}")



# import os

# # Directory containing your HTML files
# directory = 'C:/Users/punee/Desktop/coding/Website'

# # HTML content to be added (the bottom button)
# bottom_back_button_html = '''
#    <button class="back-button">Back</button>
# '''

# # Loop through all HTML files in the directory
# for filename in os.listdir(directory):
#     if filename.endswith(".html"):
#         file_path = os.path.join(directory, filename)
        
#         # Read the existing content
#         with open(file_path, 'r', encoding='utf-8') as file:
#             content = file.read()
        
#         # Check if the button is already present
#         if bottom_back_button_html.strip() not in content:
#             # Add the button before the closing </body> tag
#             content = content.replace('</body>', f'{bottom_back_button_html}\n</body>')
            
#             # Write the modified content back to the file
#             with open(file_path, 'w', encoding='utf-8') as file:
#                 file.write(content)
            
#             print(f"Added bottom back button to {filename}")
#         else:
#             print(f"Bottom back button already present in {filename}")




import os

# Directory containing your HTML files
directory = 'C:/Users/punee/Desktop/coding/Website'

# HTML content to be removed (the top right corner back button)
old_back_button_html = '''
   <button onclick="window.history.back()" style="position: fixed; top: 10px; right: 10px; background-color: #007bff; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; z-index: 1000; font-size: 1rem;">Back</button>
'''

# Loop through all HTML files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        file_path = os.path.join(directory, filename)
        
        # Read the existing content
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Remove the old back button HTML content
        if old_back_button_html in content:
            content = content.replace(old_back_button_html, '')
            
            # Write the modified content back to the file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            
            print(f"Removed old back button from {filename}")
        else:
            print(f"No old back button found in {filename}")





