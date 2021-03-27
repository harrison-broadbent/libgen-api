# LibGen Search API

___

Please ⭐ if you find this useful!
___

Four main search methods:
```python
search_title("title")
search_title_filtered("title", filters)

search_author("author")
search_author_filtered("author", filters)
```

## Basic Searching:

Search by title or author:

### Title:
```python
from libgen_api import LibgenSearch
s = LibgenSearch()
title = "some title"
s.search_title(title)
```
### Author:

```python
from libgen_api import LibgenSearch
s = LibgenSearch()
author = "some author"
s.search_author(author)
```

## Filtered Searching

- You can define a set of filters, and then use them to filter search results for both title and author searches.
- You can filter results by any combination of the values from a search.
- By default, filtering will remove results that do not match the filters exactly - filters are case-sensitive, and for numerical
  values (ID, Pages etc. ) the given value, as a string, must match exactly.
- Case-insensitive and substring filtering can be specified by passing `exact_match=False` as an argument.

### Filtered Title Searching
```python
filters = {
    "Author" 	: "Name",
    "Extension"	: "pdf"
}

from libgen_api import LibgenSearch
s = LibgenSearch()
title = "some title"
s.search_title_filtered(title, filters)
```

### Filtered Author Searching

```python
filters = {
    "Year" 		: "2002",
    "Extension"	: "mobi",
    "Pages"		: "321"
}

from libgen_api import LibgenSearch
s = LibgenSearch()
author = "some author"
s.search_author_filtered(author, filters)
```

### Results Layout
Results are returned as a list of dictionaries:
```json
[{'Author': 'John Smith',
  'Edit': 'http://example.com',
  'Extension': 'epub',
  'ID': '00000',
  'Language': 'German',
  'Mirror_1': 'http://example.com',
  'Mirror_2': 'http://example.com',
  'Mirror_3': 'http://example.com',
  'Mirror_4': 'http://example.com',
  'Mirror_5': 'http://example.com',
  'Pages': '410',
  'Publisher': 'Publisher',
  'Size': '1005 Kb',
  'Title': 'Title',
  'Year': '2021'}]
```

If there are no results, the library will return an empty array.


Check out the Design / Todo doc. [here](docs/specs.md)
