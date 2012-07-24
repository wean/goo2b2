#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import command
import utils
import logging

class CommandList(command.BaseCommand):
    """
        list 列出人员
    """

    def execute(self, client=None, db=None):
        if (client == None):
            return
        params = utils.getCommandParams(self.message)
        groups = None
        if (len(params) == 1):
            groups = client.usermanager.getUserJids(client)
        else:
            groups = client.client_roster
        if (groups == None):
            return
        msg = "\n=    User List\n"
        for jid in groups:
            name = client.client_roster[jid]["name"]
            gs = client.client_roster[jid]["groups"]
            logging.debug(gs)
            if (name == ""):
                name = jid
            msg += "=    %s %s\n" % (name, jid)
        client.sendTo(self.fjid, msg)
