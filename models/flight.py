class Flight:
    def __init__(
            self,
            origin,
            destination,
            departure_date,
            departure_time,
            arrival_time,
            airline,
            price,
            baggage,
            stops,
            duration,
            purchase_link,
    ):
        self.origin = origin
        self.destination = destination
        self.departure_date = departure_date
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.airline = airline
        self.price = price
        self.baggage = baggage
        self.stops = stops
        self.duration = duration
        self.purchase_link = purchase_link

    def display(self):
        print(f"Companhia: {self.airline}")
        print(f"Origem: {self.origin}")
        print(f"Destino: {self.destination}")
        print(f"Saída: {self.departure_time}")
        print(f"Chegada: {self.arrival_time}")
        print(f"Duração: {self.duration}")
        print(f"Bagagem: {self.baggage}")
        print(f"Escalas: {self.stops}")
        print(f"Preço: R$ {self.price}")