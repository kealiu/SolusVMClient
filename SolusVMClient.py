#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""
The SolusVM Client API SDK for Python
"""

import re
import json
import requests

class SolusClient:
    """
    SolusVM API client
    """

    def __init__(self, url, key, apihash, timeout=60):
        """
        init the SolusClient Object
        :param url: root URL, such as 'https://solusvm.com:5656'
        :param key: the API KEY, from cpanel
        :param apihash:  the API Hash, from cpanel
        :return: the new object 
        """
        self.url = url
        self.key = key
        self.hash = apihash
        self.timeout = timeout

    @staticmethod
    def _xml2dict(xmlstr):
        """
        transfer XML to dict obj
        :param xmlstr:  the XML string
        :return: the dict obj
        """
        obj = {}
        tag = re.compile('<(.*?)>([^<]+)<\/\\1>')
        length = len(xmlstr)
        pos = 0
        try:
            while pos < length:
                regex = tag.search(xmlstr, pos)
                obj[regex.group(1)] = regex.group(2)
                pos = regex.end()
        except:
            pass

        return obj

    def _post(self, action):
        """
        post data req to server
        :param action: the action that will do
        :return: the server's XML return
        """
        data={'rdtype':'json',
                'hash':self.hash,
                'key':self.key,
                'action': action}
        response = requests.post(self.url + '/api/client/command.php', 
                                    params=data, 
                                    timeout=self.timeout, 
                                    verify=False)
        return self._xml2dict(response.text)

    def info(self):
        """
        Retieve server information
        """
        return self._post('info')

    def status(self):
        """
        Retiev server status
        """
        return self._post('status')

    def reboot(self):
        """
        Reboot the server
        """
        return self._post('reboot')

    def boot(self):
        """
        Boot the server
        """
        return self._post('boot')

    def shutdown(self):
        """
        shutdown the server
        """
        return self._post('shutdown')

    def command(self, action):
        """
        run the command raw
        """
        return getattr(self, action)()

