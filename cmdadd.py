#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import command
import logging
import utils

class CommandAdd(command.BaseCommand):

    def execute(self, client=None, db=None):
        if (client != None):
            params = utils.getCommandParams(self.message)
            if (len(params) >= 2):
                new = params[1]
            else:
                return
            logging.debug(new)
            if (client.usermanager.add(client, self.fjid, new)):
                pass
