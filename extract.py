###!/usr/bin/env python3

import pypdf
import json
import re
import unidecode

import npttf2utf
mapper = npttf2utf.FontMapper("./map.json")


# Open the PDF file
file_path = './Birds_of_Nepal_An_Official_Checklist_2022.pdf'
pdf_file = open(file_path, 'rb')

# Read the PDF file
pdf_reader = pypdf.PdfReader(pdf_file)
num_pages = len(pdf_reader.pages)

# Function to extract text from each page
def extract_text(page):
    return pdf_reader.pages[page].extract_text()

# Extract text from all pages
pdf_text = [extract_text(page) for page in range(num_pages)]
pdf_text = " ".join(pdf_text)

lines = pdf_text.split('\n')
def filter_lines_starting_with_number(text):
    # Split the text into lines
    lines = text.split('\n')
    filtered_lines = []
    for line in lines:
        # Check if the line starts with a number
        if line.strip() and line.strip()[0].isdigit():
            # Find the index of "English Name"
            index = line.find("English Name")
            if index != -1:
                # Keep only the part of the line before "English Name"
                line = line[:index]
            line = re.sub(r'\ufb01\s*','fi', line)
            lineparts = line.split(' ');
            # if it is table data it must have at least 4 words (5 including the serial)
            if len(lineparts) < 5 or len(lineparts) > 10:
                continue
            second_scientific_name_idx = next((idx for idx, content in enumerate(lineparts) if content and content[0].islower()), -1)

            nepali_name_orig = ' '.join(lineparts[second_scientific_name_idx+1:len(lineparts)])
            nepali_name = unidecode.unidecode(nepali_name_orig) 
            nepali_name = mapper.map_to_unicode(nepali_name, from_font="Preeti", unescape_html_input=False, escape_html_output=False)
            nepali_name_romanized = unidecode.unidecode(nepali_name)
            filtered_lines.append({
                    'number': lineparts[0],
                    'name': ' '.join(lineparts[1:second_scientific_name_idx-1]),
                    'romanized_name': nepali_name_romanized,
                    'scientific_name': ' '.join(lineparts[second_scientific_name_idx-1:second_scientific_name_idx+1]),
                                     'extra': nepali_name  
                   })
                                                                                                                            # Join the filtered lines back into a single string
                                                                                                                
    return filtered_lines
    
# Filter lines that start with a number
filtered_lines = filter_lines_starting_with_number(pdf_text) 
    
# Join the filtered lines back into a single string
#result = '\n'
#result = result.join(filtered_lines)

# Close the PDF file
pdf_file.close()

# Print the first 2000 characters to understand the structure
print(json.dumps(filtered_lines, indent=4))

with open('birds.json', 'w', encoding='utf-8') as outfile:
    json.dump(filtered_lines, outfile, ensure_ascii=False)

#install tesseract and tessaract-lang
