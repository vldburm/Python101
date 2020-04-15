"""
Task 4

Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    # атрибуты по заданию
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # методы
    def go(self):
        return f'автомобиль {self.name} поехал'

    def stop(self):
        return f'автомобиль {self.name} остановился'

    def turn_right(self):
        return f'автомобиль {self.name} повернул направо'

    def turn_left(self):
        return f'автомобиль {self.name} повернул налево'

    def show_speed(self):
        return f'Скорость автомобиля {self.name} составляет {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'скорость городского автомобиля {self.name} составляет {self.speed}')

        if self.speed > 40:
            return f'{self.name} превысил скорость, установленную для городских автомобилей'
        else:
            return f'{self.name} двигается в пределах установленной скорости для городских автомобилей'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'скорость рабочего автомобиля {self.name} составляет {self.speed}')

        if self.speed > 60:
            return f'{self.name} превысил скорость, установленную для рабочих автомобилей'
        else:
            return f'{self.name} двигается в пределах установленной скорости для рабочих автомобилей'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полицейский авто'
        else:
            return f'{self.name} гражданский авто'


lamba = SportCar(200, 'Желтая', 'Ламба', False)
audi = TownCar(50, 'Серая', 'Ауди', False)
x5 = WorkCar(55, 'Черный', 'Х5', False)
mustang = PoliceCar(110, 'Белый', 'Мустанг', True)
print(x5.turn_left())
print(f'Когда {audi.turn_right()}, {lamba.stop()}')
print(f'{x5.go()}. {x5.show_speed()}')
print(f'{x5.name} {x5.color}')
print(f'{mustang.name} - полиция? {mustang.is_police}')
print(f'{x5.name}  - полиция? {x5.is_police}')
print(lamba.show_speed())
print(audi.show_speed())
print(mustang.police())
print(mustang.show_speed())


