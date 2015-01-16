'''
Created on Jan 15, 2015
'''
import unittest

from mandrill_open import MandrillOpen


class MandrillOpenTestCase(unittest.TestCase):
    
    def setUp(self):
        # Load from JSON string
        json_data = open('../fixtures/valid_http_post_open_track.json').read()
        self.otrack = MandrillOpen(json=json_data)
    
    def test_opening_time(self):
        self.assertEqual( self.otrack.opening_ts, 1421362071, "Opening time is wrong." )
        
    def test_user_agent(self):
        self.assertEqual( self.otrack.user_agent, "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/7.0; .NET CLR 3.0.30729; Microsoft Outlook 14.0.7113; ms-office; MSOffice 14)",
                            "User agent was read incorrectly.")     
        self.assertEqual( self.otrack.user_agent_type, "Email Client", "User Agent type is incorrect.")       
        self.assertEqual( self.otrack.user_agent_name, "Outlook 2010", "User Agent type is incorrect.")
        self.assertEqual( self.otrack.user_agent_version, None, "User Agent version is incorrect.")
        self.assertEqual( self.otrack.user_agent_os_name, "Windows 7", "OS name is incorrect.")
        self.assertEqual( self.otrack.is_mobile, False, "Is mobile? is incorrect.")

    def test_opening_ip(self):
        self.assertEqual( self.otrack.opening_ip, "200.71.135.255", "Opening IP is wrong." )
        
    def test_location(self):
        self.assertEqual( self.otrack.location_country, "United States", "Country is incorrect.")
        self.assertEqual( self.otrack.location_region, "Colorado", "Location region is incorrect.")
        self.assertEqual( self.otrack.location_city, "Denver", "Location city is incorrect.")
        self.assertEqual( self.otrack.location_lat_long, (40.647769995,-102.987762410), "Latitude and Longitude are incorrect.")

    def test_email_fields(self):
        self.assertEqual( self.otrack.email_id, "19acfd2a22247d787e2cc4890149a2d", "Email ID is incorrect.")
        self.assertEqual( self.otrack.subject, "Notification!!!11", "Email subject is incorrect.")
        self.assertEqual( self.otrack.to, "receiver@example.com", "Email TO: is incorrect.")
        self.assertEqual( self.otrack.sender, "sender@example.com", "Email FROM: is incorrect.")
        self.assertEqual( self.otrack.template, "notification", "Email FROM: is incorrect.")
        
        
        
        
