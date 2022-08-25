from time import sleep

class TrafficLight:

    def __init__(self, color):
        self.__color = color

    def running(self):
        while True:
            for key, value in self.__color.items():
                sleep(value)
                print(key)



my_traffic = TrafficLight(color={'\033[31mRed': 10, '\033[33mYellow': 7, '\033[32mGreen': 2})
my_traffic.running()






