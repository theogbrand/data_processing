import re

def clean_markdown(text):
    # Remove author section
    text = re.sub(r'\\author\{[\s\S]*?\}', '', text)
    
    # Remove English abstract section
    text = re.sub(r'\\begin\{abstract\}[\s\S]*?\\end\{abstract\}', '', text)
    
    # Remove LaTeX-style commands
    text = re.sub(r'\\[a-zA-Z]+(\{.*?\})*', '', text)
    
    # Remove Markdown formatting
    text = re.sub(r'\*+', '', text)
    text = re.sub(r'#+\s', '', text)
    
    # Remove code blocks
    text = re.sub(r'```[\s\S]*?```', '', text)
    
    # Remove empty lines and join remaining lines
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    return ' '.join(lines)

# Read the file content
with open('/data/users/brandon/ob1-projects/data_processing/md_completed/2024_10_08_d5e2bec671d0129bd68ag.mmd', 'r', encoding='utf-8') as file:
    content = file.read()

# Clean the content
cleaned_text = clean_markdown(content)

# Write the cleaned text to a new file
with open('/data/users/brandon/ob1-projects/data_processing/cleaned_output.txt', 'w', encoding='utf-8') as file:
    file.write(cleaned_text)

print("Cleaning complete. Output saved to 'cleaned_output.txt'")