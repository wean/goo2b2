#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from sleekxmpp.xmlstream.jid import JID

class UserManager:

    def __init__(self):
        pass

    def update(self, client):
        if (client == None):
            return
        groups = client.client_roster.groups()
        needUpdate = False
        for group in groups:
            if (group not in ("sub", "block", "none")):
                for jid in groups[group]:
                    client.update_roster(jid, client.client_roster[jid]["name"], None, ["none"])
                    logging.debug("Move %s to none", jid)
                    needUpdate = True
        if (needUpdate):
            client.get_roster()
            self.update(client)
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
        client.update_roster(jid, nick, "sub")
        return True
