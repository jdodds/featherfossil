from multiprocessing import Process, Queue
class InvalidArguments(ValueError):
    pass

class Plugin(Process):
    """A Plugin is a self-contained bit of functionality that runs in it's own
    process, and runs via listening for messages and sending messages through
    Queues.
    """
    listeners = None
    messengers = None
    name = 'Base Plugin'

    def __init__(self):
        """Set us up to run as a separate process, initialze our listener Queue,
        and set our runnable attribute.
        """
        super(Plugin, self).__init__()
        self.listener = Queue()
        self.runnable = True

    def set_messenger(self, messenger):
        """Set our messenger"""
        self.messenger = messenger

    def send(self, message, payload=None):
        """Send a message through our messenger Queue.
        Messages are presumably descriptions of a task that just got completed,
        or a notification of status, or whatnot.
        """
        self.messenger.put((message, payload))

    def recieve(self, message, payload=None):
        """Get a message from our listener Queue.
        This should currently be used in a subclasses self.run loop. 
        """
        self.listener.put((message, payload))

    def shutdown(self, payload):
        """Set self.runnable to false.
        This should cause a subclass to break out of it's run loop.
        """
        self.runnable=False

    def run(self):
        """This should be implemented by subclasses, and currently should loop
        until self.runnable is no longer true.
        """
        raise NotImplementedError()

