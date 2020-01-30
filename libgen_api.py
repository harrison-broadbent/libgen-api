import requests
import pandas as pd
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

def get_search_url(query, search_field='title'):
    query_parsed = "%20".join(query.split(" "))

    if search_field == 'title':
        search_url = f'http://gen.lib.rus.ec/search.php?req={query_parsed}'
        
    return search_url

# Given a title, retrieve the corresponding libgen search page. 
# Technically could search for anything as this uses the general search rather than title based search. 
# TODO: Search using the specific title search parameter. 
# TODO: Provide alternate search methods - author etc. 
def search_by_title(book_title):
    url = get_search_url(book_title, search_field='title')
    search_result = requests.get(url)
    return search_result

# given a BeautifulSoup soup, strip out all the <i> tags. 
# This is required otherwise the <i> tags interfere with getting book titles
# as they appear as subtitles on the page, however they get merged with the full title when stripped_strings is called. 
def strip_i_tag_from_soup(soup):
    subheadings = soup.find_all("i")
    for subheading in subheadings:
        subheading.decompose()

book_title = get_book_title_from_input()
soup = BeautifulSoup(search_by_title(book_title).text, 'lxml')
strip_i_tag_from_soup(soup)

# Libgen results contain 3 tables 
# Table0: Search / Logo table of information. 
# Table1: Very small table above reults table, indicating number of results 
# Table2: Table of data to scrape.
information_table = soup.find_all('table')[2]

# This code aggregates the BeautifulSoup search into structured data in the form of a nested array. 
# It also checks whether simple text or a link is being scraped and determines whether the link url (for the mirror)
# Or link text (for the title) should be preserved. 
# Both the book title and mirror links have a "title" attribute, but only the mirror links have it filled. (title vs title="libgen.io")
# Therefore we must check for a present title to ensure titles are correctly scraped. 
data = [
    [
        td.a['href'] if td.find('a') and td.find('a').has_attr("title") and td.find('a')["title"] is not "" 
        else ''.join(td.stripped_strings)
        for td in row.find_all("td")
    ]
    for row in information_table.find_all("tr")
]

link_df = pd.DataFrame(data[1:], columns=col_names)
print(link_df)
print(link_df["Title"])