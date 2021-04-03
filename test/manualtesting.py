"""

Basic testing script for libgen-api.
Runs through a number of searches using different parameters, outputs results to terminal.

Run -
python3 test.py

"""


from libgen_api.libgen_search import LibgenSearch
import json

title = "Pride and Prejudice"
author = "Agatha Christie"


# helper function to print first title if it exists.
def print_results(titles_array):
    print(json.dumps(titles_array[0], indent=1) if len(titles_array) else "No results.")
    print("\n\n--- END OF OUTPUT ---\n\n")


# test title search
# should print a result for the book specified at the top of the file.
t = LibgenSearch()
print("\n>>>\tSearching for title: " + title)

titles = t.search_title(title)
print_results(titles)


# test author search
# should print a result for the author specified at the top of the file.
a = LibgenSearch()
print("\n>>>\tSearching for author: " + author)

titles = a.search_author(author)
print_results(titles)


# test title filtering
# should print a result for the book specified at the top of the file,
# conforming to the title_filters below.
tf = LibgenSearch()
title_filters = {"Year": "2007", "Extension": "epub"}
print(
    "\n>>>\tSearching for title: "
    + title
    + " with filters --- "
    + ", ".join([":".join(i) for i in title_filters.items()])
)

titles = tf.search_title_filtered(title, title_filters, exact_match=True)
print_results(titles)


# test author filtering
# should print a result for the author specified at the top of the file,
# conforming to the title_filters below.
af = LibgenSearch()
author_filters = {"Language": "German", "Year": "2009"}
print(
    "\n>>>\tSearching for author: "
    + author
    + " with filters --- "
    + ", ".join([":".join(i) for i in author_filters.items()])
)

titles = af.search_author_filtered(author, author_filters, exact_match=True)
print_results(titles)


# test exact filtering explicitly (using an Author search)
# should print no results as the filter exclude all results.
afe = LibgenSearch()
exact_filters = {
    "Extension": "PDF"
}  # if exact_match = True, all results get filtered as "pdf" is always written lower case
print(
    "\n>>>\tSearching for author: "
    + author
    + " with filters --- "
    + ", ".join([":".join(i) for i in exact_filters.items()])
    + " & exact_match == True"
)

titles = afe.search_author_filtered(author, exact_filters, exact_match=True)
print_results(titles)


# test non-exact filtering (using an Author search)
# should print a result for the author specified at the top of the file,
# conforming to the title_filters below.
afne = LibgenSearch()
non_exact_filters = {
    "Extension": "PDF"
}  # if exact_match = True, all results get filtered as "pdf" is always written lower case
print(
    "\n>>>\tSearching for author: "
    + author
    + " with filters --- "
    + ", ".join([":".join(i) for i in non_exact_filters.items()])
    + " & exact_match == FALSE"
)

titles = afne.search_author_filtered(author, non_exact_filters, exact_match=False)
print_results(titles)


# test partial filtering (using a Title)
# should print a result for the title specified at the top of the file,
# conforming to the non_exact_filter below, with non-exact matching.
tfpne = LibgenSearch()
partial_filters = {"Extension": "p", "Year": "200"}
print(
    "\n>>>\tSearching for title: "
    + title
    + " with filters --- "
    + ", ".join([":".join(i) for i in partial_filters.items()])
    + " & exact_match == False"
)

titles = tfpne.search_title_filtered(title, partial_filters, exact_match=False)
print_results(titles)


# test partial filtering (using a Title)
# should return nothing as the extension is not an exact match to an existing one (ie. "pdf")
tfpe = LibgenSearch()
exact_partial_filters = {"Extension": "p"}
print(
    "\n>>>\tSearching for title: "
    + title
    + " with filters --- "
    + ", ".join([":".join(i) for i in exact_partial_filters.items()])
    + " & exact_match == True"
)

titles = tfpe.search_title_filtered(title, exact_partial_filters, exact_match=True)
print_results(titles)


# test resolving of mirror links
# should print a populated hash of source:download_link pairs
arml = LibgenSearch()
print("\n>>>\tSearching for title: " + title + " and resolving download links")

# Author hard-coded so that it pairs with title (currently pride and prejudice)
titles = arml.search_author("Jane Austen")
item_to_download = titles[0]
download_links = arml.resolve_download_links(item_to_download)
print_results([download_links])
