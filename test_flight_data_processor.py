import unittest
from flight_data_processor import FlightDataProcessor

class TestFlightDataProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = FlightDataProcessor()
        self.sample_flight1 = {
            "flight_number": "AZ001",
            "departure_time": "2025-02-19 15:30",
            "arrival_time": "2025-02-20 03:45",
            "duration_minutes": 735,
            "status": "ON_TIME"
        }
        self.sample_flight2 = {
            "flight_number": "AZ002",
            "departure_time": "2025-02-21 11:00",
            "arrival_time": "2025-02-21 16:00",
            "duration_minutes": 300,
            "status": "DELAYED"
        }

    def test_add_flight(self):
        self.processor.add_flight(self.sample_flight1)
        self.assertEqual(len(self.processor.flights), 1)
        self.processor.add_flight(self.sample_flight1)
        self.assertEqual(len(self.processor.flights), 1)

    def test_add_flight_missing_keys(self):
        invalid_flight = {"flight_number": "AZ003"}
        with self.assertRaises(ValueError):
            self.processor.add_flight(invalid_flight)

    def test_remove_flight(self):
        self.processor.add_flight(self.sample_flight1)
        self.processor.remove_flight("AZ001")
        self.assertEqual(len(self.processor.flights), 0)
        self.processor.remove_flight("AZ999")
        self.assertEqual(len(self.processor.flights), 0)

    def test_flights_by_status(self):
        self.processor.add_flight(self.sample_flight1)
        self.processor.add_flight(self.sample_flight2)
        on_time = self.processor.flights_by_status("ON_TIME")
        self.assertEqual(len(on_time), 1)
        self.assertEqual(on_time[0]['flight_number'], "AZ001")

    def test_get_longest_flight(self):
        self.processor.add_flight(self.sample_flight1)
        self.processor.add_flight(self.sample_flight2)
        longest = self.processor.get_longest_flight()
        self.assertEqual(longest['flight_number'], "AZ001")

    def test_get_longest_flight_empty(self):
        with self.assertRaises(ValueError):
            self.processor.get_longest_flight()

    def test_update_flight_status(self):
        self.processor.add_flight(self.sample_flight1)
        self.processor.update_flight_status("AZ001", "DELAYED")
        updated = self.processor.flights_by_status("DELAYED")
        self.assertEqual(len(updated), 1)
        self.assertEqual(updated[0]['flight_number'], "AZ001")
        with self.assertRaises(ValueError):
            self.processor.update_flight_status("AZ999", "ON_TIME")

if __name__ == '__main__':
    unittest.main()