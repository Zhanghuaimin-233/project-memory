import unittest
from src.importer import import_records


class Gateway:
    def __init__(self):
        self.calls = []

    def send_batch(self, records):
        self.calls.append(list(records))
        return {"accepted": len(records)}


class ImportTests(unittest.TestCase):
    def test_records_are_sent_in_tens_then_the_remaining_batch(self):
        gateway, store = Gateway(), []
        self.assertEqual(import_records(list(range(23)), gateway, store), 3)
        self.assertEqual(gateway.calls, [list(range(10)), list(range(10, 20)), [20, 21, 22]])
        self.assertEqual(store, [{"accepted": 10}, {"accepted": 10}, {"accepted": 3}])

    def test_empty_input_does_not_send_a_request(self):
        gateway, store = Gateway(), []
        self.assertEqual(import_records([], gateway, store), 0)
        self.assertEqual(gateway.calls, [])


if __name__ == "__main__":
    unittest.main()
