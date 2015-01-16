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
        self.assertEqual( self.otrack.opening_ts, 1421368044, "Opening time is wrong." )
        
    def test_user_agent(self):
        self.assertEqual( self.otrack.user_agent, "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.1.8) Gecko/20100317 Postbox/1.1.3", "User agent was read incorrectly.")     
        self.assertEqual( self.otrack.user_agent_type, "Email Client", "User Agent type is incorrect.")       
        self.assertEqual( self.otrack.user_agent_name, "Postbox 1.1.3", "User Agent type is incorrect.")
        self.assertEqual( self.otrack.user_agent_version, "1.1.3", "User Agent version is incorrect.")
        self.assertEqual( self.otrack.user_agent_os_name, "OS X 10.6 Snow Leopard", "OS name is incorrect.")
        self.assertEqual( self.otrack.is_mobile, False, "Is mobile? is incorrect.")

    def test_opening_ip(self):
        self.assertEqual( self.otrack.opening_ip, "127.0.0.1", "Opening IP is wrong." )
        
    def test_location(self):
        self.assertEqual( self.otrack.location_country, "United States", "Country is incorrect.")
        self.assertEqual( self.otrack.location_region, "Oklahoma", "Location region is incorrect.")
        self.assertEqual( self.otrack.location_city, "Oklahoma City", "Location city is incorrect.")
        self.assertEqual( self.otrack.location_lat_long, (35.4675598145,-97.5164337158), "Latitude and Longitude are incorrect.")

    def test_email_fields(self):
        self.assertEqual( self.otrack.email_id, "exampleaaaaaaaaaaaaaaaaaaaaaaaaa", "Email ID is incorrect.")
        self.assertEqual( self.otrack.subject, "This an example webhook message", "Email subject is incorrect.")
        self.assertEqual( self.otrack.to, "example.webhook@mandrillapp.com", "Email TO: is incorrect.")
        self.assertEqual( self.otrack.sender, "example.sender@mandrillapp.com", "Email FROM: is incorrect.")
        #self.assertEqual( self.otrack.template, "notification", "Email template is incorrect.")
        
        
        
        
