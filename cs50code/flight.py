class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = [] # flight starts without passengers
    
    def add_passenger(self, name):
        if not self.free_seats():
            return False
        self.passengers.append(name) #add a new passenger
        return True

    def free_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(4)

people = ['Andrew', 'John', 'Peter', 'Mathew']
for person in people:
    if flight.add_passenger(person):
        print(f'Added {person} to flight successfully.')
    else:
        print(f'No available seat for {person}.')