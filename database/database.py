from models.flight import Flight

FLIGHTS = [
    Flight(
        origin="Campo Grande",
        destination="São Paulo",
        departure_date="09/10/2026",
        departure_time="09:30",
        arrival_time="11:15",
        airline="LATAM",
        price=1290.90,
        baggage="1 bagagem",
        stops=0,
        duration="1h45",
        purchase_link="https://latam.com"
    ),
    Flight(
        origin="Campo Grande",
        destination="São Paulo",
        departure_date="09/10/2026",
        departure_time="14:00",
        arrival_time="15:50",
        airline="GOL",
        price=1180.00,
        baggage="Sem bagagem",
        stops=1,
        duration="1h50",
        purchase_link="https://gol.com.br"
    )
]