from database.database import FLIGHTS

def find_cheapest_flight(flights):
    cheapest_flight = flights[0]

    for flight in flights:
        if flight.price < cheapest_flight.price:
            cheapest_flight = flight

    return cheapest_flight

def find_flights(origin, destination, departure_date):

    filtered_flights = []

    for flight in FLIGHTS:
        
        if (
            flight.origin == origin and
            flight.destination == destination and
            flight.departure_date == departure_date
        ):
            filtered_flights.append(flight)

    return filtered_flights