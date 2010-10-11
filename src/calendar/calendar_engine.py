#!/usr/bin/env python

__author__ = 'aleksei.kornev@gmail.com (Aleksei Kornev)'

try:
  from xml.etree import ElementTree
except ImportError:
  from elementtree import ElementTree
import gdata.calendar.service
import gdata.service
import atom.service
import gdata.calendar
import atom
import getopt
import sys
import string
import time

import config
import event

class CalendarEngine:

	def __init__(self, email, password):
#		self.__email = email;
#		self.__password = password;
		self.cal_client = gdata.calendar.service.CalendarService()
		self.cal_client.email = email
		self.cal_client.password = password
		self.cal_client.source = 'Aleksei-Kornev'
		self.cal_client.ProgrammaticLogin()


	def addEvent(self, event):

		c_event = gdata.calendar.CalendarEventEntry();
		c_event.title = atom.Title(text=event.title);
		c_event.content = atom.Content(text=event.content);
		c_event.where.append(gdata.calendar.Where(value_string=event.location));

		if event.startTime is None:
		# Use current time for the start_time and have the event last 1 hour
			startTime = time.strftime('%Y-%m-%dT%H:%M:%S.000Z', time.gmtime());
			endTime = time.strftime('%Y-%m-%dT%H:%M:%S.000Z', time.gmtime(time.time() + 3600));
		c_event.when.append(gdata.calendar.When(start_time=startTime, end_time=endTime));
    
		new_event = self.cal_client.InsertEvent(c_event, 'http://www.google.com/calendar/feeds/gb6tsdeoca4fg35aeijf9deq78%40group.calendar.google.com/private/full');
		
		event.setUrl(new_event.GetEditLink().href);

		return event;
    

	def deleteEvent(self, event):
		self.cal_client.DeleteEvent(event.url);

	def addCalendar(self, title, description, timeZone, hidden, location, color = '#2952A3'):

		calendar = gdata.calendar.CalendarListEntry();
		calendar.title = atom.Title(text=title);
		calendar.summary = atom.Summary(text=description);
		calendar.where = gdata.calendar.Where(value_string=location);
		calendar.color = gdata.calendar.Color(value=color);
		calendar.timezone = gdata.calendar.Timezone(value=timeZone);

		if hidden:
		      calendar.hidden = gdata.calendar.Hidden(value='true');
		else:
		      calendar.hidden = gdata.calendar.Hidden(value='false');

		new_calendar = self.cal_client.InsertCalendar(new_calendar=calendar);

		return new_calendar;

if __name__ == '__main__':
	engine = CalendarEngine(config.email, config.password);
	event = engine.addEvent(event.Event('TestEvent', 'Some test event located in saratov', 'Saratov', None, None));
#	engine.deleteEvent(event);
#	print "\n\n\n\n";
#	print engine.addCalendar("TestCalendar", "It's calendar for test porpuses", "Europe/Moscow", False, "Saratov");
