import random

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = random.randint(10,100)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is driving'

    def stop(self):
        return f'and {self.name} is going to stop'

    def turn(self, direction):
        return 'to' + ' ' + direction

    def show_speed(self):
        return f'with speed {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'with speed {self.speed}')
        if self.speed > 60:
            return f'Speed of {self.name} is higher. Please, slow down'
        else:
            return f'This speed for {self.name} is normal'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'with speed {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher. Please, slow down'
        else:
            return f'This speed for {self.name} is normal'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


town = TownCar(50, 'yellow', 'Range', True)
print(town.name, town.color, town.speed, town.is_police)
print(town.go(), town.turn('right'), town.stop())
print(town.show_speed())
sport = SportCar(120, 'blue', 'F1', True)
print(sport.name, sport.color, sport.speed, sport.is_police)
print(sport.go(), sport.turn('left'), sport.stop())
work = WorkCar(45, 'white', 'Damas', False)
print(work.name, work.color, work.speed, work.is_police)
print(work.go(), work.turn('straight'), work.stop())
print(work.show_speed())
police = PoliceCar(50, 'black', 'Piu', False)
print(police.name, police.color, police.speed, police.is_police)
print(police.go(), police.turn('left'), police.stop())

