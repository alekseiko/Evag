#!/usr/bin/env python



class Event:
	
	def __init__(self, title, content, location, startTime, endTime, uri = None):
		self.title = title;
		self.content = content;
		self.location = location;
		self.startTime = startTime;
		self.endTime = endTime;
		if uri is not None:
			self.uri = uri;
