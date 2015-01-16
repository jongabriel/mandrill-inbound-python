'''
Created on Jan 15, 2015
'''
from datetime import datetime
import json


class MandrillOpen(object):

    '''
    'source' is already json while 'json' is formatted as json.
    '''
    def __init__(self, *args, **kwargs):
        if not kwargs.get('json') and not kwargs.get('source'):
            raise Exception('Mandrill Inbound Error: you must \
                            provide json or source')

        if kwargs.get('source'):
            source = kwargs.get('source')
            if source.startswith('mandrill_events='):
                source = source.replace('mandrill_events=', '') #remove the non-json start
            self.source = source
        else:
            the_json = kwargs.get('json')
            if the_json.startswith('mandrill_events='):
                the_json = the_json.replace('mandrill_events=', '') #remove the non-json start
            self.source = json.loads(the_json)[0]

        self.msg = self.source.get('msg')

        if self.source['event'] != 'open':
            raise Exception('Mandrill event not open')

    @property
    def opening_time(self):
        """
        Date/time when the open occurred.
        """
        return datetime.fromtimestamp(self.source.get('ts'))

    @property
    def opening_ts(self):
        """
        UTC unix timestamp when the event occurred
        """
        return self.source.get('ts')
        

    @property
    def user_agent(self):
        '''
        The user agent of the mail reader.
        '''
        return self.source.get('user_agent')
     
    @property
    def user_agent_type(self):
        '''
        The type of user agent (browser, Email Client, etc.)
        '''
        return self.source.get('user_agent_parsed').get('type')
           
    @property
    def user_agent_name(self):
        '''
        The name of user agent (Firefox, Chrome, Outlook)
        '''
        return self.source.get('user_agent_parsed').get('ua_name')
    
    @property
    def user_agent_version(self):
        '''
        The version of user agent
        '''
        return self.source.get('user_agent_parsed').get('ua_version')

    @property
    def user_agent_os_name(self):
        '''
        The name of the OS.
        '''
        return self.source.get('user_agent_parsed').get('os_name')
    
    @property
    def is_mobile(self):
        '''
        Was this email read on a mobile device?
        '''
        return self.source.get('user_agent_parsed').get('mobile')
    
    @property
    def opening_ip(self):
        '''
        The IP of the reading device.
        '''
        return self.source.get('ip')
    
    @property
    def location_country(self):
        '''
        The country where the email was read.
        '''
        return self.source.get('location').get('country')
    
    @property
    def location_region(self):
        '''
        The region or state where the email was read.
        '''
        return self.source.get('location').get('region')
    
    @property
    def location_city(self):
        '''
        The city where the email was read.
        '''
        return self.source.get('location').get('city')
    
    @property
    def location_lat_long(self):
        '''
        The (lat,long) where the email was read.
        Returned as a tuple, (latitude, longitude).
        '''
        lat = self.source.get('location').get('latitude')
        longitude = self.source.get('location').get('longitude')
        return (lat, longitude)
        
    @property
    def email_id(self):
        '''
        The id of the Mandrill email.
        '''
        return self.msg.get('_id')
    
    @property
    def subject(self):
        """
        The subject line of the message 
        """
        return self.msg.get('subject')
       
    @property
    def to(self):
        """
        The email address of the opened email
        """
        return self.msg.get('email')                
    
    @property
    def sender(self):
        '''
        The email address of the sender.
        '''
        return self.msg.get('sender')
    
    @property
    def template(self):
        '''
        The template used for the email.
        '''
        return self.msg.get('template')
    
    
