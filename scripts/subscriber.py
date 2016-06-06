#!/usr/bin/env python

import json
import thread
import uuid

try:
    from urllib.request import urlopen
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse
    from urllib2 import urlopen

__all__ = ["NotifyPublisher"]

class NotifySubscriber():
    def __init__(self, **kwargs):
        self.channel = kwargs.get("channel", self.default_channel)
        self.host = kwargs.get("host", "localhost")
        self.port = kwargs.get("port", 80)
        self.ssl = kwargs.get("ssl", False)
        assert type(self.port) == int
        assert self.ssl in [True, False]
        thread.start_new_thread(self.listen, ())

    @property
    def default_channel(self):
        return str(uuid.uuid1())

    @property
    def url(self):
        return "{protocol}://{host}:{port}/sub/{channel}".format(
                protocol=["http","https"][self.ssl],
                host=self.host,
                port=self.port,
                channel=self.channel
                )

    def listen(self):
        print "listening", self.url
        feed = urlopen(self.url, timeout=2)
        buff = ""
        while True:
            ch =  feed.read(1)
            if ch == "\n":
                self.handler(buff)
                buff = ""
            else:
                buff += ch


    def handler(self, message):
        print message



if __name__ == "__main__":
    import time
    config = json.load(open("local_settings.json"))
    notify = NotifySubscriber(**config)
    while True:
        time.sleep(1)
