# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio.rest.base import Domain
from twilio.rest.taskrouter.v1 import V1


class Taskrouter(Domain):

    def __init__(self, twilio):
        super(Taskrouter, self).__init__(twilio)
        
        self.base_url = 'https://taskrouter.twilio.com'
        """ :type : str """
        self._v1 = None
        """ :type : twilio.rest.taskrouter.v1.V1 """

    @property
    def v1(self):
        """
        :returns: Version v1 of taskrouter
        :rtype: twilio.rest.taskrouter.v1.V1
        """
        if self._v1 is None:
            self._v1 = V1(self)
        return self._v1

    @property
    def workspaces(self):
        """
        :rtype: twilio.rest.taskrouter.v1.workspace.WorkspaceList
        """
        return self.v1.workspaces

    def __repr__(self):
        return '<Twilio.Taskrouter>'
