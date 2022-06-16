import requests
from bs4 import BeautifulSoup

from .search_request import SearchRequest

MIRROR_SOURCES = ["GET", "Cloudflare", "IPFS.io", "Infura"]


class LibgenSearch:
    def search_title(self, query):
        search_request = SearchRequest(query, search_type="title")
        return search_request.aggregate_request_data()

    def search_author(self, query):
        search_request = SearchRequest(query, search_type="author")
        return search_request.aggregate_request_data()

    def search_title_filtered(self, query, filters, exact_match=True):
        search_request = SearchRequest(query, search_type="title")
        results = search_request.aggregate_request_data()
        filtered_results = filter_results(
            results=results, filters=filters, exact_match=exact_match
        )
        return filtered_results

    def search_author_filtered(self, query, filters, exact_match=True):
        search_request = SearchRequest(query, search_type="author")
        results = search_request.aggregate_request_data()
        filtered_results = filter_results(
            results=results, filters=filters, exact_match=exact_match
        )
        return filtered_results

    def resolve_download_links(self, item):
        mirror_1 = item["Mirror_1"]
        page = requests.get(mirror_1)
        soup = BeautifulSoup(page.text, "html.parser")
        links = soup.find_all("a", string=MIRROR_SOURCES)
        download_links = {link.string: link["href"] for link in links}
        return download_links


# def filter_results(results, filters, exact_match):
#     """
#     Returns a list of results that match the given filter criteria.
#     When exact_match = true, we only include results that exactly match
#     the filters (ie. the filters are an exact subset of the result).

#     When exact-match = false,
#     we run a case-insensitive check between each filter field and each result.

#     exact_match defaults to TRUE -
#     this is to maintain consistency with older versions of this library.
#     """
#     filtered_list = []
#     filter_matches_result = False
#     for result in results:
#         for field, query in filters.items():
#             if exact_match:
#                 if result[field] in query:
#                     filter_matches_result = True
#                 else:
#                     filter_matches_result = False
#                     break
#             else:
#                 if type(query) is list:
#                     for item in query:
#                         if item.casefold() in result[field].casefold():
#                             filter_matches_result = True
#                             break
#                         if not filter_matches_result:
#                             break
#                 elif (
#                     type(query) is str and query.casefold() in result[field].casefold()
#                 ):
#                     filter_matches_result = True
#                 else:
#                     filter_matches_result = False
#                     break
#         if filter_matches_result:
#             filtered_list.append(result)

#     return filtered_list

def filter_results(results, filters, exact_match):
    """
    Returns a list of results that match the given filter criteria.
    When exact_match = true, we only include results that exactly match
    the filters (ie. the filters are an exact subset of the result).

    When exact-match = false,
    we run a case-insensitive check between each filter field and each result.

    exact_match defaults to TRUE -
    this is to maintain consistency with older versions of this library.
    """

    # helper func 1
    def get_match_bln(field_filter, result_field, exact_match):
        match_bln = False
        if not exact_match:
            match_bln = field_filter.casefold() in result_field.casefold()
        else:
            match_bln = field_filter == result_field
        return match_bln

    # helper func 2
    def get_filtered_result(result, filters, exact_match):
        filtered_results = []
        for field, field_filter in filters.items():

            # case 1: list filter
            if isinstance(field_filter, list):
                field_filter_list = field_filter
                filtered_results = any({get_match_bln(field_filter, result[field], exact_match) for field_filter in field_filter_list})

            # case 2: str filter
            elif isinstance(field_filter, str):
                filtered_results = get_match_bln(field_filter, result[field], exact_match)

            # break if result found
            if filtered_results:
                break

        return any(filtered_results)

    # body
    filtered_list = []
    for result in results:
        if get_filtered_result(result, filters, exact_match):
            filtered_list.append(result)

    return filtered_list
