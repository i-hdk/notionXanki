'''
HOW TO USE:
    1. INSIDE YOUR NOTION PAGE, COPY THE TOGGLE LISTS. MAKE SURE TO ONLY COPY THE TOGGLE LISTS AND NOTHING ELSE
    2. PASTE IN 'notionRaw.txt'
    3. RUN THIS FILE
    4. OPEN ANKI, IMPORT 'toggle_output.csv' 
    5. SET FIELD SEPARATER TO COMMA 
'''

# Open the file in read mode ('r')
file_path = 'notionRaw.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    # Read the entire content of the file
    content = file.read()
    
#print(content)

titles = []
descriptions = []
lines = content.splitlines()
desc = ""
firstDesc = True

for line in lines:
    #print(line)
    if line[0] == '-':
        titles.append(line[2:])
        if not firstDesc:
            descriptions.append(desc)
        firstDesc = False
        desc = ""
    else:
        desc+=line+"\n"

descriptions.append(desc)
#print(titles)
#3print(descriptions)

import csv

# Ensure both lists have the same length
assert len(titles) == len(descriptions), "Lists must be of equal length."

# Open a CSV file for writing
with open('toggle_output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    # Create a CSV writer object
    writer = csv.writer(csvfile)    
    # Iterate over the lists and write each pair as a row
    for title, description in zip(titles, descriptions):
        writer.writerow([title, description])

print("CSV file created successfully.")


