from bs4 import BeautifulSoup
import re
import os


print('What directory would you like to update?\n  - publications\n  - presentations\n')
update_direc = input()

if not os.path.isdir(f'_{ update_direc }'):
    os.mkdir(f'_{ update_direc }')

print('What zotero export file (HTML) would you like to parse?')
for file in os.listdir('zotero_export'):
    print(f'  - { file }')
export_file = input()

with open(f'zotero_export/{ export_file }', "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    divs = soup.find_all('div',{"class": "csl-entry"})
    for div in divs:
        text = div.text
        year = re.search(r'\d{4}', text).group(0)
        author = text.split(", ")[0]
        title = re.search(r'“(.*?)”', text).group(0).strip('“').strip('”')[:-1].replace(" ", "_")
        if not os.path.isdir(f'_{ update_direc }/{ year }'):
            os.mkdir(f'_{ update_direc }/{ year }')
        with open(f'_{ update_direc }/{ year }/{ author }_{ title }_{ year }.md', 'w') as p:
            p.write(f'---\npresentation_year: { year }\n---\n{ text }\n')
        # print(text, year, author, title)
