#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Goo2b2
"""

import sys
import getpass

import sleekxmpp
import event

if sys.version_info < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf8')
else:
    raw_input = input

class Client(sleekxmpp.ClientXMPP):

    def __init__(self, jid, password):
        sleekxmpp.ClientXMPP.__init__(self, jid, password)
        self.event = event.Event(self)
