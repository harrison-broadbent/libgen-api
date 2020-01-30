import requests
import pandas as pd
from bs4 import BeautifulSoup

LANGUAGE = "English"
TYPE = "pdf"
col_names = ["ID", "Author", "Title", "Publisher", "Year", "Pages", "Language", "Size", "Extension", 
            "Mirror_1", "Mirror_2", "Mirror_3", "Mirror_4", "Mirror_5", "Edit"]

book_name = "the killing floor"
# book_name = "eragon"

book_name_parsed = "%20".join(book_name.split(" "))

search_url = f'http://gen.lib.rus.ec/search.php?req={book_name_parsed}'

search_result = requests.get(search_url)

soup = BeautifulSoup(search_result.text, 'lxml')
subheadings = soup.find_all("i")
for subheading in subheadings:
   subheading.decompose()

information_table = soup.find_all('table')[2]

data1 = []
for row in information_table.find_all('tr'):
    col_array = []
    for td in row.find_all("td"):
        if td.find('a') and td.find('a').has_attr("title") and td.find('a')["title"] is not "":
            col_array.append(td.a['href'])
        else:
            col_array.append(''.join(td.stripped_strings))
    data1.append(col_array)

link_dfn = pd.DataFrame(data1[1:], columns=col_names)
print(link_dfn["Title"])