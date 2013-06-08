# Copyright (c) 2013 Christopher Kaster (@Kasoki)
# 
# This file is part of alfred.py <https://github.com/Kasoki/alfred.py>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import os

""" IMPORTANT: Not sure how to use this lib? Check out the "example.py" file :) """

Version="0.2"

class Handler:
	""" Alfred.Handler, this class is responsible for handling Alfred! """

	def __init__(self, args=[], query="", use_no_query_string=True):
		""" Create a new handler

		Keyword arguments:
		args -- This list should be *sys.argv* (default: [])
		query -- This string should only be used if args is not set!
		use_no_query_string -- If there is no query, should the handler use "NO QUERY" instead of one?

		""" 
		if type(args) != list:
			raise TypeError("Alfred.Handler(args): args is no list!")

		if len(args) > 1:
			self.query = args[1]
		elif query != "":
			self.query = query
		else:
			if use_no_query_string:
				self.query = "EMPTY_QUERY"
			else:
				self.query = ""

		self.items = []

	def get_current_directory(self):
		return os.getcwd()

	def query_is_empty(self):
		if self.query == "EMPTY_QUERY" or self.query == "":
			return True
		else:
			return False

	def add_item(self, item):
		""" Adds a new Alfred.Item to this handler

		Keyword arguments:
		item -- The Alfred.Item you want to add ;)

		"""
		if not isinstance(item, Item):
			raise TypeError("Alfred.Handler.add_item(item): item is no instance of Alfred.Item")

		self.items.append(item)

	def add_new_item(self, title="", subtitle="", uid=None, arg="", icon=None):
		""" Adds a new Item to this handler without using the Alfred.Item class!

		Keyword arguments:
		title -- The title of this item
		subtitle -- The subtitle of this item
		uid -- The uid of this item (default: None)
		arg -- The argument of this item
		icon -- The icon of this item (Default: None)

		"""
		self.add_item(Item(title, subtitle, uid, arg, icon))

	def __str__(self):
		return self.to_xml()

	def to_xml(self, max_results=None):
		""" Generates a XML string

		Keyword arguments:
		max_results -- How many results should be in this string? (Default: None - No limitation)

		"""
		xml_string = '<?xml version="1.0" encoding="UTF-8" ?>'

		xml_string += '<items>'

		counter = 0

		for item in self.items:
			xml_string += item.__str__()

			counter += 1

			if max_results is not None and counter >= max_results:
				break

		xml_string += '</items>'

		return xml_string

	def push(self, max_results=None):
		""" Push the content to Alfred

		Keyword arguments:
		max_results -- How many results should be in this string? (Default: None - No limitation)

		"""
		print(self.to_xml(max_results))

	def test_push(self, max_results=None):
		""" Sometimes it's faster to just do stuff in your editor instead of opening Alfred ;)

		Keyword arguments:
		max_results -- How many results should be in this string? (Default: None - No limitation)
		
		"""

		counter = 1

		for item in self.items:
			print("Entry #%s:" % counter)
			print("\tTitle: %s" % item.title)
			print("\tSubtitle: %s" % item.subtitle)
			print("\tArguments: %s, Icon: %s" % (item.arg, item.icon))
			print("-"*30)

			counter += 1



class Item:
	def __init__(self, title="", subtitle="", uid=None, arg="", icon=None):
		""" Creates a new Item for Alfred

		Keyword arguments:
		title -- The title of this item
		subtitle -- The subtitle of this item
		uid -- The uid of this item (default: None)
		arg -- The argument of this item
		icon -- The icon of this item (Default: None)

		"""
		self.title = title
		self.subtitle = subtitle
		self.uid = uid
		self.arg = arg
		self.icon = icon

	def __str__(self):
		title = '<title>%s</title>' % self.title
		subtitle = '<subtitle>%s</subtitle>' % self.subtitle
		icon = ''
		args = ''

		if self.icon is not None:
			icon = '<icon>%s</icon>' % self.icon

		if self.arg is not None:
			args = '<arg>%s</arg>' % self.arg

		item_content = "%s%s%s%s" % (title, subtitle, icon, args)

		item_info = '<item uid="%s">%s</item>' % (self.uid, item_content)

		return item_info
