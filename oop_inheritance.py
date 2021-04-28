class Robot:

    def __init__(self, name, version):
        self.name = name
        self.version = version

    def move_forward(self):
        print(f'{self.name} is moving forward!')

    def move_backward(self):
        print(f'{self.name} is moving backward!')

    def move_right(self):
        print(f'{self.name} is moving right!')

    def move_left(self):
        print(f'{self.name} is moving left!')


class HouseBot(Robot):
    def __init__(self, name, version, area_covered):
        super().__init__(name, version)
        self.area_covered = area_covered

    def clean(self):
        if self.area_covered > 0:
            print(f'{self.name} is cleaning the house!')
            self.area_covered -= 30

            if self.area_covered < 0:
                self.area_covered = 0

        else:
            print('CANNOT CLEAN!, PLEASE RESET THE AREA COVERED PARAMETER')

    def set_cover_area(self, area):
        if self.area_covered == 0:
            self.area_covered = area
        else:
            print('I CAN STILL CLEAN MORE AREA!')

    @staticmethod
    def halt():
        print('I am halting.')

    # overriding the forward method
    def move_forward(self):
        print('This is in House Bot class!')
        super().move_forward()


class MaidBot(HouseBot):
    def __init__(self, name, version, area_covered, cooking):
        super().__init__(name, version, area_covered)
        self.cooking = cooking


m = MaidBot('a', 1.1, 10, 'noodles')

houseBot = HouseBot('Bob', 1.1, 50)
robo = Robot('Stan lee', 1.5)
# print(houseBot.name)
# print(houseBot.version)
# houseBot.move_forward()
# houseBot.move_right()
# houseBot.clean()
# houseBot.clean()
# houseBot.clean()
# print(houseBot.area_covered)
# houseBot.set_cover_area(50)
# houseBot.clean()

# print(help(Robot))
# print(help(HouseBot))

print(issubclass(HouseBot, Robot))
print(issubclass(Robot, HouseBot))
print(issubclass(Robot, object))
print(issubclass(HouseBot, object))

print(isinstance(houseBot, Robot))
print(isinstance(houseBot, HouseBot))

print(isinstance(houseBot, object))
print(isinstance(robo, object))
