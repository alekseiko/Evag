#!/usr/bin/env python

class Calendar:
	
	def __init__(self, title, desc, location, color, timeZone, isHidden = 'true', uri = '/calendar/feeds/default/private/full'):
		self.title = title;
		self.uri = uri;
		self.desc = desc;
		self.location = location;
		self.color = color;
		self.timeZone = timeZone;
		self.isHidden = isHidden;
