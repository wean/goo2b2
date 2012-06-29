#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import command
import logging

class CommandNick(command.BaseCommand):

    def execute(self, client=None, db=None):
        if (client != None):
            idx = self.message.find(" ")
            if (idx < 0):
                return
            nick = self.message[idx + 1:]
            idx = nick.find(" ")
            if (idx > 0):
                nick = nick[:idx]
            logging.debug(nick)
            if (client.usermanager.changeName(client, self.fjid, nick)):
                pass
