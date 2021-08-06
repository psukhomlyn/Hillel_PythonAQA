"""
Описать транспортное средство. Можете брать любое на свое усмотрение.
Хочу видеть наследование (обычное с несколькими уровнями иерархии),
абстракцию, сокрытие, инкапсуляцию.
"""


class Car:
    def __init__(self, color: str, engine_volume: int, wheels: int,
                 producer: str, speed: int, passengers: int):
        self.color = color
        self.engine_volume = engine_volume
        self.wheels = wheels
        self.producer = producer
        self.speed = speed
        self.passengers = passengers

    def drive_forward(self):
        raise NotImplementedError("Not implemented")  #abstraction


class Truck(Car):
    def __init__(self, color: str, engine_volume: int, wheels: int,
                 producer: str, speed: int, passengers: int, power: int,
                 length: int):
        super().__init__(color, engine_volume, wheels, producer, speed,
                         passengers)
        self.power = power
        self.length = length

    def drive_forward(self):
        print("Truck is driving forward")

    def _shipping(self):
        print("Truck is shipping cargo")



class RacingTruck(Truck):
    def __init__(self, color: str, engine_volume: int, wheels: int,
                 producer: str, speed: int, passengers: int, power: int,
                 length: int, weight: int):
        super(RacingTruck, self).__init__(color, engine_volume, wheels,
                                          producer, speed, passengers, power,
                                          length)
        self.weight = weight

    def drive_racing(self):
        print("Truck is in racing")




if __name__ == '__main__':
    Volvo_truck = Truck("silver", 5000, 12, "Volvo", 70, 3, 500, 15)
    print(Volvo_truck.color)
    print(Volvo_truck.speed)
    print(Volvo_truck.power)
    Volvo_truck.drive_forward()
    Volvo_truck._shipping()

    Racing_Volvo = RacingTruck("red", 2000, 12, "Volvo", 250, 1, 1500, 5, 1200)
    print(Racing_Volvo.color, Racing_Volvo.engine_volume)
    print(Racing_Volvo.weight)
# Good but I don't see hiding abstraction and incapsulation
# -6 points