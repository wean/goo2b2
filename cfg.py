#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Cfg:

    def __init__(self):
        self.CommandPrefix = "#"

    def cfg():
        if ("instance" not in dir(Cfg)):
            Cfg.instance = Cfg()
        return Cfg.instance
