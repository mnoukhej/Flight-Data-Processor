# Flight Data Processor

## Overview

The **Flight Data Processor** is a Python class designed to manage and process flight data. It provides methods to add, remove, query, and update flight information, ensuring clean coding practices and robust functionality. The project also includes comprehensive unit tests to validate the correctness and stability of the implementation.

---

## Features

The `FlightDataProcessor` class supports the following operations:

1. **Add a Flight**:
   - Adds a new flight to the list.
   - Ensures no duplicate flight numbers are added.
   - Validates that all required flight details are present.

2. **Remove a Flight**:
   - Removes a flight by its flight number.

3. **Query Flights by Status**:
   - Returns all flights with a specified status (e.g., "ON_TIME", "DELAYED", "CANCELLED").

4. **Get the Longest Flight**:
   - Returns the flight with the longest duration in minutes.

5. **Update Flight Status**:
   - Updates the status of an existing flight by its flight number.

---

## Requirements

- Python 3.6 or higher.
- The `unittest` library (included in Python's standard library).

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/flight-data-processor.git