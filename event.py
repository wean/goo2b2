#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
        pass

    def changed_subscription(self, e):
        pass

    def chatstate_active(self, e):
        pass

    def chatstate_composing(self, e):
        pass

    def chatstate_gone(self, e):
        pass

    def chatstate_inactive(self, e):
        pass

    def chatstate_paused(self, e):
        pass

    def connected(self, e):
        pass

    def disco_info(self, e):
        pass

    def disco_items(self, e):
        pass

    def disconnected(self, e):
        pass

    def entity_time(self, e):
        pass

    def failed_auth(self, e):
        pass

    def gmail_messages(self, e):
        pass

    def gmail_notify(self, e):
        pass

    def got_offline(self, e):
        pass

    def got_online(self, e):
        pass

    def groupchat_direct_invite(self, e):
        pass

    def groupchat_invite(self, e):
        pass

    def groupchat_message(self, e):
        pass

    def groupchat_presence(self, e):
        pass

    def groupchat_subject(self, e):
        pass

    def killed(self, e):
        pass

    def last_activity(self, e):
        pass

    def message(self, e):
        print(e)

    def message_form(self, e):
        pass

    def message_xform(self, e):
        pass

    def presence_available(self, e):
        pass

    def presence_error(self, e):
        pass

    def presence_form(self, e):
        pass

    def presence_probe(self, e):
        pass

    def presence_subscribe(self, e):
        pass

    def presence_subscribed(self, e):
        pass

    def presence_unavailable(self, e):
        pass

    def presence_unsubscribe(self, e):
        pass

    def presence_unsubscribed(self, e):
        pass

    def roster_update(self, e):
        pass

    def sent_presence(self, e):
        pass

    def session_end(self, e):
        pass

    def session_start(self, e):
        self.client.send_presence()
        self.client.get_roster()

    def socket_error(self, e):
        pass

    def stream_error(self, e):
        pass


if (__name__ == "__main__"):
    e = Event(None)

