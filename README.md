# LibGen Search API

- Only grabs the first page of results (max 25)
- Currently only searches by title
- Built as I had reliability issues with similar offerings (and because libgen is epic)

Check out the Design / Todo doc. [here](docs/specs.md)

USAGE:

    from libgen_api import LibgenSearch
    s = LibgenSearch()
    title = "some title"
    s.search_title(title)

OUTPUT:

    [
    	{
    		'ID': 'ID',
    		'Author': 'Author',
    		'Title': 'Title',
    		'Publisher': 'Name',
    		'Year': 'Year',
    		'Pages': 'Pages',
    		'Language': 'Lang',
    		'Size': 'X Mb',
    		'Extension': 'Extension',
    		'Mirror_1': 'URL1',
    		'Mirror_2': 'URL2',
    		'Mirror_3': 'URL3',
    		'Mirror_4': 'URL4',
    		'Mirror_5': 'URL5',
    	},
    	{
    		...,
    		...,
    		...
    	},
    	...
    ]

If there are no results, search_title() will return an empty array.

    []
