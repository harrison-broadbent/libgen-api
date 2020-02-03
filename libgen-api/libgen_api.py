# TODO: encapsulate everything in a class and turn into a library

import requests
from bs4 import BeautifulSoup

LANGUAGE = "English"
TYPE = "pdf"
col_names = ["ID", "Author", "Title", "Publisher", "Year", "Pages", "Language", "Size", "Extension", 
            "Mirror_1", "Mirror_2", "Mirror_3", "Mirror_4", "Mirror_5", "Edit"]

# Get user input via terminal to get book title to search
def get_book_title_from_input():
    print("Please enter the book title: ")
    book_title = input(">>> ")
    return book_title

# TODO: Search using the specific title search parameter. 
# TODO: Provide alternate search methods - author etc.                      
def get_search_page(query, search_field='title'):
    query_parsed = "%20".join(query.split(" "))

    if search_field == 'title':
        search_url = f'http://gen.lib.rus.ec/search.php?req={query_parsed}'

    search_page = requests.get(search_url)
    return search_page

# This is required otherwise the <i> tags interfere with getting book titles
# as they appear as subtitles on the page, however they get merged with the full title when stripped_strings is called. 
def strip_i_tag_from_soup(soup):
    subheadings = soup.find_all("i")
    for subheading in subheadings:
        subheading.decompose()

def aggregate_request_data(request_search_object):
    soup = BeautifulSoup(request_search_object.text, 'lxml')
    strip_i_tag_from_soup(soup)

    # Libgen results contain 3 tables 
    # Table2: Table of data to scrape.
    information_table = soup.find_all('table')[2]

    # checks whether simple text or a link is being scraped and determines whether the link url (for the mirror)
    # Or link text (for the title) should be preserved. 
    # Both the book title and mirror links have a "title" attribute, but only the mirror links have it filled. (title vs title="libgen.io")
    raw_data = [
        [
            td.a['href'] if td.find('a') and td.find('a').has_attr("title") and td.find('a')["title"] is not "" 
            else ''.join(td.stripped_strings)
            for td in row.find_all("td")
        ]
        for row in information_table.find_all("tr")[1:] # Skip row 0 as it is the headings row
    ]

    output_data = [
        dict(zip(col_names, row))  for row in raw_data
    ]

    return output_data

def search(query, search_field="title", file_type="", language=""):
    search_page = get_search_page(book_title, search_field="title")
    output_data = aggregate_request_data(search_page)
    return output_data


book_title = get_book_title_from_input()
output_data = search(book_title)
print(output_data[0])
