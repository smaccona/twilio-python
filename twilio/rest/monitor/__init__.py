# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio.rest.base import Domain
from twilio.rest.monitor.v1 import V1


class Monitor(Domain):

    def __init__(self, twilio):
        super(Monitor, self).__init__(twilio)
        
        self.base_url = 'https://monitor.twilio.com'
        """ :type : str """
        self._v1 = None
        """ :type : twilio.rest.monitor.v1.V1 """

    @property
    def v1(self):
        """
        :returns: Version v1 of monitor
        :rtype: twilio.rest.monitor.v1.V1
        """
        if self._v1 is None:
            self._v1 = V1(self)
        return self._v1

    @property
    def alerts(self):
        """
        :rtype: twilio.rest.monitor.v1.alert.AlertList
        """
        return self.v1.alerts

    @property
    def events(self):
        """
        :rtype: twilio.rest.monitor.v1.event.EventList
        """
        return self.v1.events

    def __repr__(self):
        return '<Twilio.Monitor>'
