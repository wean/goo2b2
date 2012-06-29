#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

class EventHandler:

    def __init__(self, client):
        self.client = client
        for name in (dir(self)):
            if (name[:2] == "__"):
                continue
            event = getattr(self, name)
            if (callable(event) == False):
                continue
            if (self.client):
                self.client.add_event_handler(name, event)

    def changed_status(self, e):
        logging.debug("TODO: changed_status")
        logging.debug(e)

    def changed_subscription(self, e):
        print("TODO: changed_subscription")
        print(e)

    def chatstate_active(self, e):
        print("TODO: chatstate_active")
        print(e)

    def chatstate_composing(self, e):
        print("TODO: chatstate_composing")
        print(e)

    def chatstate_gone(self, e):
        print("TODO: chatstate_gone")
        print(e)

    def chatstate_inactive(self, e):
        print("TODO: chatstate_inactive")
        print(e)

    def chatstate_paused(self, e):
        print("TODO: chatstate_paused")
        print(e)

    def connected(self, e):
        print("TODO: connected")
        print(e)

    def disco_info(self, e):
        print("TODO: disco_info")
        print(e)

    def disco_items(self, e):
        print("TODO: disco_items")
        print(e)

    def disconnected(self, e):
        print("TODO: disconnected")
        print(e)

    def entity_time(self, e):
        print("TODO: entity_time")
        print(e)

    def failed_auth(self, e):
        print("TODO: failed_auth")
        print(e)

    def gmail_messages(self, e):
        print("TODO: gmail_messages")
        print(e)

    def gmail_notify(self, e):
        print("TODO: gmail_notify")
        print(e)

    def got_offline(self, e):
        print("TODO: got_offline")
        print(e)

    def got_online(self, e):
        print("TODO: got_online")
        print(e)

    def groupchat_direct_invite(self, e):
        print("TODO: groupchat_direct_invite")
        print(e)

    def groupchat_invite(self, e):
        print("TODO: groupchat_invite")
        print(e)

    def groupchat_message(self, e):
        print("TODO: groupchat_message")

    def groupchat_presence(self, e):
        print("TODO: groupchat_presence")

    def groupchat_subject(self, e):
        print("TODO: groupchat_subject")

    def killed(self, e):
        print("TODO: killed")

    def last_activity(self, e):
        print("TODO: last_activity")

    def message(self, e):
        logging.debug(e["type"])
        if (e["type"] in ("chat", "normal")):
            logging.debug(e["body"])

    def message_form(self, e):
        print("TODO: message_form")

    def message_xform(self, e):
        print("TODO: message_xform")

    def presence_available(self, e):
        print("TODO: presence_available")

    def presence_error(self, e):
        print("TODO: presence_error")

    def presence_form(self, e):
        print("TODO: presence_form")

    def presence_probe(self, e):
        print("TODO: presence_probe")

    def presence_subscribe(self, e):
        print("TODO: presence_subscribe")

    def presence_subscribed(self, e):
        print("TODO: presence_subscribed")

    def presence_unavailable(self, e):
        print("TODO: presence_unavailable")

    def presence_unsubscribe(self, e):
        print("TODO: presence_unsubscribe")

    def presence_unsubscribed(self, e):
        print("TODO: presence_unsubscribed")

    def roster_update(self, e):
        print("TODO: roster_update")

    def sent_presence(self, e):
        print("TODO: sent_presence")

    def session_end(self, e):
        print("TODO: session_end")

    def session_start(self, e):
        self.client.send_presence()
        self.client.get_roster()

    def socket_error(self, e):
        print("TODO: socket_error")

    def stream_error(self, e):
        print("TODO: stream_error")


if (__name__ == "__main__"):
    e = Event(None)

