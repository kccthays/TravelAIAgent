from models.flight import Flight

def find_cheapest_flight(flights):
    cheapest_flight = flights[0]

    for flight in flights:
        if flight.price < cheapest_flight.price:
            cheapest_flight = flight

    return cheapest_flight

def find_flights(origin, destination, departure_date):

    flights = []

    flight1 = Flight(
        origin=origin,
        destination=destination,
        departure_date=departure_date,
        departure_time="09:30",
        arrival_time="11:15",
        airline="LATAM",
        price=1290.90,
        baggage="1 bagagem",
        stops=0,
        duration="1h45",
        purchase_link="https://latam.com"
    )

    flight2 = Flight(
        origin=origin,
        destination=destination,
        departure_date=departure_date,
        departure_time="14:00",
        arrival_time="15:50",
        airline="GOL",
        price=1180.00,
        baggage="Sem bagagem",
        stops=1,
        duration="1h50",
        purchase_link="https://gol.com.br"
    )

    flights.append(flight1)
    flights.append(flight2)

    return flights