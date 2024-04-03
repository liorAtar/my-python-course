# Task One: Use Python to extract the Google Drive link from the .csv file.
# (Hint: It`s along the diagonal from top left to bottom right).

import csv

link_file = open('Exercise_Files/find_the_link.csv', encoding="utf-8")
csv_content = csv.reader(link_file)

google_link = []
for idx, data in enumerate(list(csv_content)):
    google_link.append(data[idx])

print(''.join(google_link))

# Task Two: Download the PDF from the Google Drive link
# (we already downloaded it for you just in case you can't download from Google Drive)
# and find the phone number that is in the document.
# Note: There are different ways of formatting a phone number!

import PyPDF2
import re

file = open('Exercise_Files/find_the_Phone_Number.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(file)

all_content = ''
for page in pdf_reader.pages:
    all_content += page.extract_text()

patter = r'\d{3}\W\d{3}\W\d{4}'
phone = re.search(patter, all_content)

print(phone.group()[:3] + ' ' + phone.group()[4:7] + ' ' + phone.group()[8:12])


