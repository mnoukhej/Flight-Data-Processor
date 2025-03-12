from typing import List, Dict

class FlightDataProcessor:
    def __init__(self) -> None:
        self.flights: List[Dict] = []

    def add_flight(self, data: Dict) -> None:
        required_keys = {'flight_number', 'departure_time', 'arrival_time', 'duration_minutes', 'status'}
        
        if not required_keys.issubset(data.keys()):
            raise ValueError("Missing required flight data keys")
        
        if any(flight['flight_number'] == data['flight_number'] for flight in self.flights):
            return
        self.flights.append(data)

    def remove_flight(self, flight_number: str) -> None:
        self.flights = [flight for flight in self.flights if flight['flight_number'] != flight_number]

    def flights_by_status(self, status: str) -> List[Dict]:
        return [flight for flight in self.flights if flight['status'] == status]


    def get_longest_flight(self) -> Dict:
        if not self.flights:
            raise ValueError("No flights available")
        
        return max(self.flights, key=lambda x: x['duration_minutes'])

    def update_flight_status(self, flight_number: str, new_status: str) -> None:
        for flight in self.flights:
            if flight['flight_number'] == flight_number:
                flight['status'] = new_status
                return
        
        raise ValueError(f"Flight {flight_number} not found")   