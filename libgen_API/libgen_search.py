from .search_request import SearchRequest
import requests
from bs4 import BeautifulSoup

class LibgenSearch:
	
	def search_title(self, query):
		self.search_request = SearchRequest(query, search_type="title")
		return self.search_request.aggregate_request_data()

	def search_author(self, query):
		self.search_request = SearchRequest(query, search_type="author")
		return self.search_request.aggregate_request_data()

	def search_title_filtered(self, query, filters = {	"ID": "",
														"Author": "", 
														"Title": "", 
														"Publisher": "", 
														"Year": "",
														"Pages": "",
														"Language": "",
														"Size": "",
														"Extension": "", 
														"Mirror_1": "",
														"Mirror_2": "",
														"Mirror_3": "",
														"Mirror_4": "",
														"Mirror_5": "",
														"Edit": ""	
														}):
		self.search_request = SearchRequest(query, search_type="title")
		data = self.search_request.aggregate_request_data()
		
		filtered_data = data
		for f in filters:
			filtered_data = [d for d in filtered_data if d[f] in filters.values()]
		return filtered_data

	def search_author_filtered(self, query, filters = {	"ID": "",
														"Author": "", 
														"Title": "", 
														"Publisher": "", 
														"Year": "",
														"Pages": "",
														"Language": "",
														"Size": "",
														"Extension": "", 
														"Mirror_1": "",
														"Mirror_2": "",
														"Mirror_3": "",
														"Mirror_4": "",
														"Mirror_5": "",
														"Edit": ""	
														}):
		self.search_request = SearchRequest(query, search_type="author")
		data = self.search_request.aggregate_request_data()
		
		filtered_data = data
		for f in filters:
			filtered_data = [d for d in filtered_data if d[f] in filters.values()]
		return filtered_data
		
