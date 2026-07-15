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

    print("\n===== VOOS ENCONTRADOS =====")

    for flight in flights:
        print(f"\nCompanhia: {flight.airline}")
        print(f"Preço: R$ {flight.price}")

    if len(flights) == 0:
        print("❌ Nenhum voo encontrado.")
        return

    cheapest_flight = find_cheapest_flight(flights)

    print("===== MELHOR VOO =====")
    print(f"Companhia: {cheapest_flight.airline}")
    print(f"Preço: R$ {cheapest_flight.price}")
    print(f"Quantidade de voos encontrados: {len(flights)}")


if __name__ == "__main__":
    main()