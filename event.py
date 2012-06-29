#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Event:

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

    def changed_status(self, event):
        pass

    def changed_subscription(self, event):
        pass

    def chatstate_active(self, event):
        pass

    def chatstate_composing(self, event):
        pass

    def chatstate_gone(self, event):
        pass

    def chatstate_inactive(self, event):
        pass

    def chatstate_paused(self, event):
        pass

    def connected(self, event):
        pass

    def disco_info(self, event):
        pass

    def disco_items(self, event):
        pass

    def disconnected(self, event):
        pass

    def entity_time(self, event):
        pass

    def failed_auth(self, event):
        pass

    def gmail_messages(self, event):
        pass

    def gmail_notify(self, event):
        pass

    def got_offline(self, event):
        pass

    def got_online(self, event):
        pass

    def groupchat_direct_invite(self, event):
        pass

    def groupchat_invite(self, event):
        pass

    def groupchat_message(self, event):
        pass

    def groupchat_presence(self, event):
        pass

    def groupchat_subject(self, event):
        pass

    def killed(self, event):
        pass

    def last_activity(self, event):
        pass

    def message(self, event):
        pass

    def message_form(self, event):
        pass

    def message_xform(self, event):
        pass

    def presence_available(self, event):
        pass

    def presence_error(self, event):
        pass

    def presence_form(self, event):
        pass

    def presence_probe(self, event):
        pass

    def presence_subscribe(self, event):
        pass

    def presence_subscribed(self, event):
        pass

    def presence_unavailable(self, event):
        pass

    def presence_unsubscribe(self, event):
        pass

    def presence_unsubscribed(self, event):
        pass

    def roster_update(self, event):
        pass

    def sent_presence(self, event):
        pass

    def session_end(self, event):
        pass

    def session_start(self, event):
        pass

    def socket_error(self, event):
        pass

    def stream_error(self, event):
        pass


if (__name__ == "__main__"):
    e = Event(None)

