def strip_i_tag_from_soup(soup):
	subheadings = soup.find_all("i")
	for subheading in subheadings:
		subheading.decompose()

