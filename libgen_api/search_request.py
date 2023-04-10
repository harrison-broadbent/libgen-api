import requests
from bs4 import BeautifulSoup
import urllib.parse

# WHY
# The SearchRequest module contains all the internal logic for the library.
#
# This encapsulates the logic,
# ensuring users can work at a higher level of abstraction.

# USAGE
# req = search_request.SearchRequest("[QUERY]", search_type="[title]")


class SearchRequest:

    col_names = [
        "ID",
        "Author",
        "Title",
        "Publisher",
        "Year",
        "Pages",
        "Language",
        "Size",
        "Extension",
        "Mirror_1",
        "Mirror_2",
        "Mirror_3",
        "Mirror_4",
        "Mirror_5",
        "Edit",
    ]

    def __init__(self, query, search_type="title"):
        self.query = query
        self.search_type = search_type

        if len(self.query) < 3:
            raise Exception("Query is too short")

    def strip_i_tag_from_soup(self, soup):
        subheadings = soup.find_all("i")
        for subheading in subheadings:
            subheading.decompose()

    def get_search_page(self):
        query_parsed = "%20".join(self.query.split(" "))
        if self.search_type.lower() == "title":
            search_url = (
                f"http://gen.lib.rus.ec/search.php?req={query_parsed}&column=title"
            )
        elif self.search_type.lower() == "author":
            search_url = (
                f"http://gen.lib.rus.ec/search.php?req={query_parsed}&column=author"
            )
        search_page = requests.get(search_url)
        return search_page


    def add_direct_download_links(self, output_data):
        # Add a direct download link to each result
        for book in output_data:
            id = book["ID"]
            download_id = str(id)[:-3] + "000"
            md5 = book["Mirror_1"].split("/")[-1].lower()
            title = urllib.parse.quote(book["Title"])
            extension = book["Extension"]
            book['Direct_Download_Link'] = f"http://62.182.86.140/main/{download_id}/{md5}/{title}.{extension}"

        return output_data

    def aggregate_request_data(self):
        search_page = self.get_search_page()
        soup = BeautifulSoup(search_page.text, "lxml")
        self.strip_i_tag_from_soup(soup)

        # Libgen results contain 3 tables
        # Table2: Table of data to scrape.
        information_table = soup.find_all("table")[2]

        # Determines whether the link url (for the mirror)
        # or link text (for the title) should be preserved.
        # Both the book title and mirror links have a "title" attribute,
        # but only the mirror links have it filled.(title vs title="libgen.io")
        raw_data = [
            [
                td.a["href"]
                if td.find("a")
                and td.find("a").has_attr("title")
                and td.find("a")["title"] != ""
                else "".join(td.stripped_strings)
                for td in row.find_all("td")
            ]
            for row in information_table.find_all("tr")[
                1:
            ]  # Skip row 0 as it is the headings row
        ]

        output_data = [dict(zip(self.col_names, row)) for row in raw_data]

        output_data = self.add_direct_download_links(output_data)

        return output_data
