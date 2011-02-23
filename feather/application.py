import collections
from feather.dispatcher import Dispatcher

class Application(object):

    def __init__(self, commands):
        self.dispatcher = Dispatcher()

        self.needed_listeners = set(commands)
        self.needed_listeners.add('APP_START')

        self.needed_messengers = set(commands)
        self.needed_messengers.add('APP_END')

        self.valid = False

    def register(self, plugin):
        self.needed_listeners -= plugin.listeners
        self.needed_messengers -= plugin.messengers

        if self.needed_messengers == self.needed_listeners == set():
            self.valid = True

        self.dispatcher.register(plugin)

    def start(self):
        self.dispatcher.start()
        
