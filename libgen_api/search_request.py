import requests
from bs4 import BeautifulSoup
import re

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
            text = subheading.text.strip()
            # Check if text resembles an ISBN pattern
            if not re.match(r'^[\d\-X,\s]+$', text):
                subheading.decompose()

    def get_search_page(self):
        query_parsed = "%20".join(self.query.split(" "))
        if self.search_type.lower() == "title":
            search_url = (
                f"https://libgen.is/search.php?req={query_parsed}&column=title"
            )
        elif self.search_type.lower() == "author":
            search_url = (
                f"https://libgen.is/search.php?req={query_parsed}&column=author"
            )
        search_page = requests.get(search_url)
        return search_page

    def aggregate_request_data(self):
        search_page = self.get_search_page()
        soup = BeautifulSoup(search_page.text, "lxml")
        self.strip_i_tag_from_soup(soup)

        information_table = soup.find_all("table")[2]

        raw_data = [
            [
                td.a["href"]
                if td.find("a")
                and td.find("a").has_attr("title")
                and td.find("a")["title"] != ""
                else "".join(td.stripped_strings)
                for td in row.find_all("td")
            ]
            for row in information_table.find_all("tr")[1:]
        ]

        output_data = []
        for row in raw_data:
            title = row[2]
            title = self.insert_space_before_digit(title)
            row[2] = title
            output_data.append(dict(zip(self.col_names, row)))

        return output_data
