#!/usr/bin/env python

import json
import uuid

try:
    from urllib.request import urlopen
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse
    from urllib2 import urlopen

__all__ = ["NotifyPublisher"]

class NotifyPublisher():
    def __init__(self, **kwargs):
        self.channel = kwargs.get("channel", self.default_channel)
        self.host = kwargs.get("host", "localhost")
        self.port = kwargs.get("port", 80)
        self.ssl = kwargs.get("ssl", False)
        assert type(self.port) == int
        assert self.ssl in [True, False]

    @property
    def default_channel(self):
        return str(uuid.uuid1())

    @property
    def url(self):
        return "{protocol}://{host}:{port}/pub?id={channel}".format(
                protocol=["http","https"][self.ssl],
                host=self.host,
                port=self.port,
                channel=self.channel
                )

    def send(self, message):
        print "sending to", self.url, ":", message
        post_data = json.dumps(message) + "\n"
        result = urlopen(self.url, post_data, timeout=1)


if __name__ == "__main__":
    import time
    try:
        config = json.load(open("local_settings.json"))
    except:
        config = {}
    print config
    print type(config["host"])
    notify = NotifyPublisher(**config)
    while True:
        notify.send("Hello. It is {}".format(time.strftime("%H:%M:%S")))
        time.sleep(1)
