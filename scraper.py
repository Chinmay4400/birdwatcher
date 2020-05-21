import requests
from bs4 import BeautifulSoup

URL = "https://www.kolkatabirds.com/citibirds.html"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

name_elements = soup.find_all(class_ = 'textstyle14')
scientific_name_elements = soup.find_all(class_ = 'textstyle17')

names = []
for span in name_elements:
    names.append(span.text.replace('-',' '))
    if(names[-1].strip()==''):
        names.pop()
        continue

sci_names = []
for span in scientific_name_elements:
    sci_names.append(span.text.replace('-',' '))
    if(sci_names[-1].strip()==''):
        sci_names.pop()
        continue

queries = []
for name, sci_name in zip(names,sci_names):
    queries.append(name+" "+sci_name)

with open("queries.txt", 'w') as f:
    for each in queries:
        f.write(f"{each}\n")
