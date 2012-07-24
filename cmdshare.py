#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import command
import logging
import utils
import urllib.request
from xml.dom.minidom import parseString

class CommandShare(command.BaseCommand):

    def execute(self, client=None, db=None):
        if (client != None):
            params = utils.getCommandParams(self.message)
            if (len(params) >= 2):
                url = params[1]
            else:
                return
            #user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
            #headers = {'User-Agent' : user_agent}
            #req = urllib.request.Request(url, None, headers)
            #res = urllib.request.urlopen(req)
            #page = res.read()
            #print(page.decode("utf8"))

            opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
            remote = opener.open(url)
            page = remote.read()
            dom = parseString(page)
            title = dom.getElementByTagName('title')
            if(title && len(title) > 0):
                print(title[0])
