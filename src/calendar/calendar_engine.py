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
import calendar

class CalendarEngine:

	def __init__(self, email, password):
#		self.__email = email;
#		self.__password = password;
		self.cal_client = gdata.calendar.service.CalendarService()
		self.cal_client.email = email
		self.cal_client.password = password
		self.cal_client.source = 'Aleksei-Kornev'
		self.cal_client.ProgrammaticLogin()


	def addEvent(self, event, calendar = None):
		c_event = gdata.calendar.CalendarEventEntry();
		c_event.title = atom.Title(text=event.title);
		c_event.content = atom.Content(text=event.content);
		c_event.where.append(gdata.calendar.Where(value_string=event.location));

		if event.startTime is None:
		# Use current time for the start_time and have the event last 1 hour
			startTime = time.strftime('%Y-%m-%dT%H:%M:%S.000Z', time.gmtime());
			endTime = time.strftime('%Y-%m-%dT%H:%M:%S.000Z', time.gmtime(time.time() + 3600));
		c_event.when.append(gdata.calendar.When(start_time=startTime, end_time=endTime));
    
		if calendar is None:
		#Add to default calendar
			uri = '/calendar/feeds/default/private/full';
		else:
			uri = calendar.uri

		new_event = self.cal_client.InsertEvent(c_event, uri);
		
		event.uri =  new_event.GetEditLink().href;

		return event;
    

	def deleteEvent(self, event):
		self.cal_client.DeleteEvent(event.uri);

	def addCalendar(self,calendar):

		gcalendar = gdata.calendar.CalendarListEntry();
		gcalendar.title = atom.Title(text=calendar.title);
		gcalendar.summary = atom.Summary(text=calendar.desc);
		gcalendar.where = gdata.calendar.Where(value_string=calendar.location);
		gcalendar.color = gdata.calendar.Color(value=calendar.color);
		gcalendar.timezone = gdata.calendar.Timezone(value=calendar.timeZone);

		gcalendar.hidden = gdata.calendar.Hidden(value=calendar.isHidden);

		new_calendar = self.cal_client.InsertCalendar(new_calendar=gcalendar);

		calendar.uri = new_calendar.GetEditLink().href;

		print dir(new_calendar);

		return calendar;

	def deleteCalendar(self, calendar):
		self.cal_client.Delete(calendar.uri);

if __name__ == '__main__':
	engine = CalendarEngine(config.email, config.password);
#	event = engine.addEvent(event.Event('TestEvent', 'Some test event located in saratov', 'Saratov', None, None));
#	engine.deleteEvent(event);
#	print "\n\n\n\n";
	cal = engine.addCalendar(calendar.Calendar("TestCalendar", "It's calendar for test porpuses", "Saratov", "#A32929", "Europe/Moscow", 'false'));
	print cal.uri
	event = engine.addEvent(event.Event('TestEvent', 'Some test event located in saratov', 'Saratov', None, None), cal);

#	engine.deleteCalendar(cal);
