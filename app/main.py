from services.flight_service import (
    find_cheapest_flight,
    find_flights
)

def main():
    origin = input("Origem: ")
    destination = input("Destino: ")
    departure_date = input("Data da viagem: ")

    flights = find_flights(
        origin,
        destination,
        departure_date
    )
    
    flights.sort(key=lambda flight: flight.price)

    if len(flights) == 0:
        print("❌ Nenhum voo encontrado.")
        return

        print("\n==== VOOS ENCONTRADOS ====")

    for index, flight in enumerate(flights, start=1):
        print(f"\nVoo {index}")
        print(flight)

    cheapest_flight = find_cheapest_flight(flights)

    print("\n===== MELHOR OPÇÃO =====")
    print(f"Companhia: {cheapest_flight.airline}")
    print(f"Preço: R$ {cheapest_flight.price}")
    print(f"Link: {cheapest_flight.purchase_link}")


if __name__ == "__main__":
    main()
