from multiprocessing import Process, Queue
class InvalidArguments(ValueError):
    pass

class Plugin(Process):
    listeners = None
    messengers = None
    name = 'Base Plugin'

    def __init__(self):
        super(Plugin, self).__init__()
        self.listener = Queue()
        self.alive = True

    def set_messenger(self, messenger):
        self.messenger = messenger

    def send(self, message, payload=None):
        self.messenger.put((message, payload))

    def recieve(self, message, payload=None):
        self.listener.put((message, payload))

    def shutdown(self, payload):
        self.alive=False

    def run(self):
        while True:
            message, payload = self.listener.get()
            if message == 'APP_STOP':
                return

