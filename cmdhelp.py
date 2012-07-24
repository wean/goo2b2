#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import command

class CommandHelp(command.BaseCommand):

    helpText = None

    def execute(self, client=None, db=None):
        if (CommandHelp.helpText == None):
            CommandHelp.helpText = "";
            for cmd in command.GooCommands:
                if (command.GooCommands[cmd].__doc__):
                    CommandHelp.helpText += "\n" + command.GooCommands[cmd].__doc__;
        if (client != None):
            client.sendTo(self.fjid, CommandHelp.helpText)
