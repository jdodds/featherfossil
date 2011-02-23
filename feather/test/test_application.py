import unittest
from feather import Application, Plugin

class ApplicationTest(unittest.TestCase):

    def setUp(self):
        self.commands = set(['one', 'two', 'three', 'APP_START'])
        self.app = Application(self.commands)
        
    def test_create_application(self):
        self.assertEqual(self.app.needed_listeners, self.commands)
        self.assertEqual(self.app.needed_messengers, self.commands)
        self.assertFalse(self.app.valid)

    def tet_valid_app(self):
        plugin = Plugin(listeners=['one'], messengers=['two'])
        self.app.register(plugin)

        self.assertNotIn('one', self.app.needed_listeners)
        self.assertIn('one', self.app.needed_messengers)

        self.assertNotIn('two', self.app.needed_messengers)
        self.assertIn('two', self.app.needed_listeners)

        self.assertFalse(self.app.valid)

        plugin = Plugin(listeners=['two', 'three'],
                        messengers=['two', 'three'])
        self.app.register(plugin)

        self.assertNotIn('two', self.app.needed_messengers)
        self.assertNotIn('two', self.app.needed_listeners)
        self.assertNotIn('three', self.app.needed_listeners)
        self.assertNotIn('three', self.app.needed_messengers)

        self.assertFalse(self.app.valid)

        plugin = Plugin(listeners=['one'], messengers=['one'])
        self.app.register(plugin)
        
        self.assertNotIn('one', self.app.needed_messengers)
        self.assertNotIn('one', self.app.needed_listeners)

        self.assertTrue(self.app.valid)
