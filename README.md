# LibGen Search API

Please ⭐ if you find this useful!

Four main search methods: 
	
	search_title("title")
	search_title_filtered("title", filters)
	
	search_author("author")
	search_author_filtered("author", filters)

## Basic Searching:

- Search by title or author - 

	### Title:

			from libgen_api import LibgenSearch
			s = LibgenSearch()
			title = "some title"

			s.search_title(title)

	### Author:

		from libgen_api import LibgenSearch
		s = LibgenSearch()
		author = "some author"

		s.search_author(author)

## Filtered Searching

- You can define a set of filters, and then use them to filter search results for both title and author searches.
- You can filter results by any combination of the values from a search.
- Filtering will remove results that do not match the filters exactly - filters are case sensitive, and for numerical values (ID, Pages etc. ) the given value, as a string, must match exactly. 

	### Filtered Title Searching

		filters = {
			"Author" 	: "Name",
			"Extension"	: "pdf"
		}

		from libgen_api import LibgenSearch
		s = LibgenSearch()
		title = "some title"
		s.search_title_filtered(title, filters)

	### Filtered Author Searching

		filters = {
			"Year" 		: "2002",
			"Extension"	: "mobi",
			"Pages"		: "321"
		}

		from libgen_api import LibgenSearch
		s = LibgenSearch()
		author = "some author"
		s.search_author_filtered(author, filters)

## Results Layout

    [
    	{
    		'ID'		: 'ID',
    		'Author'	: 'Author',
    		'Title'		: 'Title',
    		'Publisher'	: 'Name',
    		'Year'		: 'Year',
    		'Pages'		: 'Pages',
    		'Language'	: 'Lang',
    		'Size'		: 'X',
    		'Extension'	: 'Extension',
    		'Mirror_1'	: 'URL1',
    		'Mirror_2'	: 'URL2',
    		'Mirror_3'	: 'URL3',
    		'Mirror_4'	: 'URL4',
    		'Mirror_5'	: 'URL5',
    		'Edit'		: 'edit_URL'

    	},
    	{
    		...,
    		...,
    		...
    	},
    	...
    ]

If there are no results, the library will return an empty array.

    []

Check out the Design / Todo doc. [here](docs/specs.md)
