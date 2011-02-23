class InvalidArguments(ValueError):
    pass

class Plugin(object):
    listeners = None
    messengers = None

    def set_messenger(self, messenger):
        self.messenger = messenger

    def send(self, message, payload=None):
        self.messenger.put((message, payload))

    def recieve(self, message, payload=None):
        raise NotImplementedError()
    
