#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cfg import Cfg
import logging
import sys,os

GooCommands = {}


class BaseCommand:
    """
        基本消息Command
    """
    def __init__(self, jid, message):
        self.fjid = jid
        self.message = message

    def execute(self, client=None, db=None):
        if (client != None):
            client.sendToOther(self.fjid, self.message)

def LoadCommand():
    """
        预加载Command
    """
    cmdPath = sys.path[0]
    if (os.path.isdir(cmdPath)):
        fileList = os.listdir(cmdPath)
        for fileItem in fileList:
            if (fileItem[:3] == "cmd" and fileItem[-3:] == ".py"):
                cmdName = fileItem[3:-3]
                m = None
                try:
                    m = __import__(fileItem[:-3])
                except:
                    logging.debug(fileItem + " Load Faild!")
                if (m == None):
                    continue
                CommandName = "Command" + cmdName[:1].upper() + cmdName[1:]
                if (CommandName not in dir(m)):
                    logging.debug(CommandName + " Command File Syntax Error !")
                    continue
                cls = getattr(m, CommandName)
                if (cls == None):
                    continue
                if (not callable(cls)):
                    logging.debug(CommandName + " Command Is Not Callable !")
                    continue
                GooCommands[cmdName] = cls

def CreateCommand(jid, message):
    """
        按照消息创建新Command的实例
    """
    if (message[:1] == Cfg.cfg().CommandPrefix):
        idx = message.find(" ")
        if (idx > 0):
            commandName = message[1:idx]
        else:
            commandName = message[1:]
        if (commandName in GooCommands):
            cls = GooCommands[commandName]
            return cls(jid, message)

    return BaseCommand(jid, message)
