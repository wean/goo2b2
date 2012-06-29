#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cfg import Cfg
import logging

class BaseCommand:

    def __init__(self, jid, message):
        self.fjid = jid
        self.message = message

    def execute(self, client=None, db=None):
        if (client != None):
            client.sendToOther(self.fjid, self.message)

def CreateCommand(jid, message):
    if (message[:1] == Cfg.cfg().CommandPrefix):
        idx = message.find(" ")
        if (idx > 0):
            commandName = message[1:idx]
        else:
            commandName = message[1:]
        m = None
        try:
            m = __import__("cmd" + commandName)
        except:
            logging.debug("cmd" + commandName + " does not support!")
        if (m != None):
            className = "Command" + commandName[:1].upper() + commandName[1:]
            if (className in dir(m)):
                cls = getattr(m, className)
                if (callable(cls)):
                    return cls(jid, message);

    return BaseCommand(jid, message)
