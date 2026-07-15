from models.flight import Flight


def main():

    flight = Flight(
        origin="Campo Grande",
        destination="São Paulo",
        departure_date="10/10/2026",
        departure_time="09:30",
        arrival_time="11:15",
        airline="LATAM",
        price=1290.90,
        baggage="1 bagagem",
        stops=0,
        duration="1h45",
        purchase_link="https://latam.com"
    )

    print("===== PRIMEIRO VOO =====")
    print(f"Origem: {flight.origin}")
    print(f"Destino: {flight.destination}")
    print(f"Preço: R$ {flight.price}")
    print(f"Companhia: {flight.airline}")


if __name__ == "__main__":
    main()