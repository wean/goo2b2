#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import command

class CommandHelp(command.BaseCommand):

    def execute(self, client=None, db=None):
        if (client != None):
            client.send_message(mto=self.fjid, 
                    mbody=self.message,
                    mtype="chat")
