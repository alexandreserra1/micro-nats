import unittest
from main import NumberEvent

class TestNumberEvent(unittest.TestCase):
    def test_number_event(self):
        event = NumberEvent(number=123, timestamp=1617181723.0)
        self.assertEqual(event.number, 123)
        self.assertEqual(event.timestamp, 1617181723.0)

if __name__ == '__main__':
    unittest.main()
