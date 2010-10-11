#!/usr/bin/env python



class Event:
	
	def __init__(self, title, content, location, startTime, endTime):
		self.title = title;
		self.content = content;
		self.location = location;
		self.startTime = startTime;
		self.endTime = endTime;

	def setUrl(self, url):
		self.url = url

