from collections import defaultdict
from Queue import Empty
from multiprocessing import Queue

import sys

class Dispatcher(object):
    def __init__(self):
        self.listeners = defaultdict(set)
        self.plugins = set()
        self.messages = Queue()

    def register(self, plugin):
        for listener in plugin.listeners:
            self.listeners[listener].add(plugin)
        self.plugins.add(plugin)
        plugin.set_messenger(self.messages)
        plugin.start()

    def start(self):
        self.recieve('APP_START')
        self.alive = True
        while self.alive:
            message, payload = self.messages.get()
            if message == 'APP_STOP':
                for plugin in self.plugins:
                    print 'shutting down %s' % plugin
                    plugin.recieve('SHUTDOWN')
                self.alive = False
            else:
                self.recieve(message, payload)

    def recieve(self, message, payload=None):
        print 'got %s %s' % (message, payload)
        print 'have %d listeners to send to' % len(self.listeners[message])
        for listener in self.listeners[message]:
            print 'sending to %s' % listener
            listener.recieve(message, payload)



        
