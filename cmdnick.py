#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import command
import logging
import utils

class CommandNick(command.BaseCommand):

    def execute(self, client=None, db=None):
        if (client != None):
            params = utils.getCommandParams(self.message)
            if (len(params) >= 2):
                nick = params[1]
            else:
                return
            logging.debug(nick)
            if (client.usermanager.changeName(client, self.fjid, nick)):
                pass
