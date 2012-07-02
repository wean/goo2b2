#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import command
import utils

class CommandBan(command.BaseCommand):

    def execute(self, client=None, db=None):
        if (client == None):
            return
        params = utils.getCommandParams(self.message)
        if (len(params) < 2):
            return
        client.usermanager.ban(client, self.fjid, params[1])
