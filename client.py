#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Goo2b2
"""

import logging
import sleekxmpp
from event import EventHandler
from usermanager import UserManager
from sleekxmpp.jid import JID

class Client(sleekxmpp.ClientXMPP):

    def __init__(self, jid, password):
        sleekxmpp.ClientXMPP.__init__(self, jid, password)
        self.register_plugin('xep_0030') # Service Discovery
        self.register_plugin('xep_0047', {
            'accept_stream': self.accept_stream
        }) # In-band Bytestreams
        self.eventhandler = EventHandler(self)
        self.usermanager = UserManager()

    def accept_stream(self, iq):
        return True

    def sendToOther(self, jid, message):
        j = JID(jid)
        jid = j.user + "@" + j.domain
        name = self.client_roster[jid]["name"]
        if (name == ""):
            name = jid
        for toj in self.usermanager.getUserJids(self):
            if (toj == jid):
                continue
            self.sendTo(toj, "[" + name + "]" + message)

    def sendTo(self, jid, message):
        if (isinstance(jid, JID)):
            jid = jid.user + "@" + jid.domain
        self.send_message(mto=jid.strip(),
                mbody=message,
                mtype="chat")
