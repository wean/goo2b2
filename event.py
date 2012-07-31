#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import command

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
        logging.debug("TODO: changed_subscription")
        logging.debug(e)

    def chatstate_active(self, e):
        logging.debug("TODO: chatstate_active")
        logging.debug(e)

    def chatstate_composing(self, e):
        logging.debug("TODO: chatstate_composing")
        logging.debug(e)

    def chatstate_gone(self, e):
        logging.debug("TODO: chatstate_gone")
        logging.debug(e)

    def chatstate_inactive(self, e):
        logging.debug("TODO: chatstate_inactive")
        logging.debug(e)

    def chatstate_paused(self, e):
        logging.debug("TODO: chatstate_paused")
        logging.debug(e)

    def connected(self, e):
        logging.debug("TODO: connected")
        logging.debug(e)

    def disco_info(self, e):
        logging.debug("TODO: disco_info")
        logging.debug(e)

    def disco_items(self, e):
        logging.debug("TODO: disco_items")
        logging.debug(e)

    def disconnected(self, e):
        logging.debug("TODO: disconnected")
        logging.debug(e)

    def entity_time(self, e):
        logging.debug("TODO: entity_time")
        logging.debug(e)

    def failed_auth(self, e):
        logging.debug("TODO: failed_auth")
        logging.debug(e)

    def gmail_messages(self, e):
        logging.debug("TODO: gmail_messages")
        logging.debug(e)

    def gmail_notify(self, e):
        logging.debug("TODO: gmail_notify")
        logging.debug(e)

    def got_offline(self, e):
        logging.debug("TODO: got_offline")
        logging.debug(e)

    def got_online(self, e):
        logging.debug("TODO: got_online")
        logging.debug(e)

    def groupchat_direct_invite(self, e):
        logging.debug("TODO: groupchat_direct_invite")
        logging.debug(e)

    def groupchat_invite(self, e):
        logging.debug("TODO: groupchat_invite")
        logging.debug(e)

    def groupchat_message(self, e):
        logging.debug("TODO: groupchat_message")
        logging.debug(e)

    def groupchat_presence(self, e):
        logging.debug("TODO: groupchat_presence")
        logging.debug(e)

    def groupchat_subject(self, e):
        logging.debug("TODO: groupchat_subject")
        logging.debug(e)

    def killed(self, e):
        logging.debug("TODO: killed")
        logging.debug(e)

    def last_activity(self, e):
        logging.debug("TODO: last_activity")
        logging.debug(e)

    def message(self, e):
        if (e["type"] in ("chat", "normal")):
            c = command.CreateCommand(e["from"], e["body"])
            if (c != None):
                c.execute(self.client)

    def message_form(self, e):
        logging.debug("TODO: message_form")
        logging.debug(e)

    def message_xform(self, e):
        logging.debug("TODO: message_xform")
        logging.debug(e)

    def presence_available(self, e):
        logging.debug("TODO: presence_available")
        logging.debug(e)

    def presence_error(self, e):
        logging.debug("TODO: presence_error")
        logging.debug(e)

    def presence_form(self, e):
        logging.debug("TODO: presence_form")
        logging.debug(e)

    def presence_probe(self, e):
        logging.debug("TODO: presence_probe")
        logging.debug(e)

    def presence_subscribe(self, e):
        logging.debug("TODO: presence_subscribe")
        logging.debug(e)

    def presence_subscribed(self, e):
        logging.debug("TODO: presence_subscribed")
        logging.debug(e)

    def presence_unavailable(self, e):
        logging.debug("TODO: presence_unavailable")
        logging.debug(e)

    def presence_unsubscribe(self, e):
        logging.debug("TODO: presence_unsubscribe")
        logging.debug(e)

    def presence_unsubscribed(self, e):
        logging.debug("TODO: presence_unsubscribed")
        logging.debug(e)

    def roster_update(self, e):
        logging.debug("TODO: roster_update")
        logging.debug(e)

    def sent_presence(self, e):
        logging.debug("TODO: sent_presence")
        logging.debug(e)

    def session_end(self, e):
        logging.debug("TODO: session_end")
        logging.debug(e)

    def session_start(self, e):
        self.client.send_presence()
        self.client.get_roster()
        self.client.usermanager.update(self.client)

    def socket_error(self, e):
        logging.debug("TODO: socket_error")
        logging.debug(e)

    def stream_error(self, e):
        logging.debug("TODO: stream_error")
        logging.debug(e)

    def ibb_stream_start(self, e):
        logging.debug("TODO: ibb_stream_start")
        logging.debug(e)

    def ibb_stream_data(self, e):
        logging.debug("TODO: ibb_stream_data")
        logging.debug(e)

    def disco_info(self, e):
        logging.debug("TODO: disco_info")
        logging.debug(e)

    def disco_items(self, e):
        logging.debug("TODO: disco_items")
        logging.debug(e)

if (__name__ == "__main__"):
    e = Event(None)

