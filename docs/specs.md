## API Layout

    [
    	[
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
    		'Mirror_5': 'URL5', }
    	],
    	[
    		...,
    		...,
    		...
    	],
    	...
    ]

- All fields are strings
- If a value is not present, the field will contain an empty string
- Some listings will have page count listed in the form of "count[secondary-count]" as this is how they appear on LibGen.
  \_ Only the first page of results (max. 25) will be returned.

## Ideas for project

- Specify libgen url domains to use (incase one goes down)
- Filter by language, type etc.
- Detect how many pages of results there are and search them all.
- May cast types directly (string to int for ID etc. ), however assuming everything is strings seems easier.
- Handle 404 / Timeout errors better
