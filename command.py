#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cfg

class BaseCommand:

    def __init__(self, jid, message):
        self.fjid = jid
        self.message = message

    def execute(self):
        logging.debug("Execute ", self.fjid, self.message)

def CreateCommand(jid, message):
    if (message[:1] == cfg.CommandPrefix):
        pass
    else:
        return BaseCommand(jid, message)
