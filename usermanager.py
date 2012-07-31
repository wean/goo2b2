#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from sleekxmpp.jid import JID

class UserManager:

    def __init__(self):
        pass

    def update(self, client):
        if (client == None):
            return

    def getUserJids(self, client):
        if (client == None):
            return
        groups = client.client_roster.groups()
        if ("sub" in groups):
            return groups["sub"]

    def changeName(self, client, jid, nick):
        if (client == None):
            return None
        if (len(nick) > 50):
            return False
        j = JID(jid)
        jid = j.user + "@" + j.domain
        groups = client.client_roster.groups()
        if (jid not in groups["sub"]):
            return False
        client.update_roster(jid, name=nick, subscription="both", groups=["sub"])
        return True

    def ban(self, client, jid, banid):
        if (client == None):
            return None
        if (banid == None):
            return None
        groups = client.client_roster.groups()
        client.update_roster(banid, subscription="both", groups=["block"])
        return True

    def add(self, client, jid, newid):
        if (client == None):
            return None
        if (newid == None):
            return None
        client.update_roster(newid, subscription="both", groups=["sub"])
        client.send_presence(pto=newid, ptype='subscribe')
        return True
