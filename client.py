#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Goo2b2
"""

import sleekxmpp
from event import EventHandler

class Client(sleekxmpp.ClientXMPP):

    def __init__(self, jid, password):
        sleekxmpp.ClientXMPP.__init__(self, jid, password)
        self.eventhandler = EventHandler(self)
