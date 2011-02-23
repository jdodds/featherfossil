from collections import defaultdict
from Queue import Empty
from multiprocessing import Queue

class Dispatcher(object):
    def __init__(self):
        self.listeners = defaultdict(set)
        self.messages = Queue()

    def register(self, plugin):
        for listener in plugin.listeners:
            self.listeners[listener].add(plugin)

    def start(self):
        self.recieve('APP_START')
        while True:
            message, payload = self.messages.get()
            if message == 'APP_STOP':
                return
            self.recieve(message, payload)

    def recieve(self, message, payload=None):
        q = Queue()
        for listener in self.listeners[message]:
            listener.set_messenger(q)
            listener.recieve(message, payload)
        try:
            while self.messages.put(q.get(timeout=0.5)):
                continue
        except Empty:
            return

        
