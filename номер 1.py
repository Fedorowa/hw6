from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 3:
            print('Горит свет: ', TrafficLight.__color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(3)
            i += 1


light = TrafficLight()
light.running()
