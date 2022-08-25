class Stationary:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return '\033[37mзапуск отрисовки'

class Pen(Stationary):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return "\033[34mдля конспектов"


class Pencil(Stationary):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return '\033[35mдля рисования'


class Handle(Stationary):

    def __int__(self, title):
        super().__init__(title)

    def draw(self):
        return '\033[36mдля заметок'


kans = Stationary('\033[37mКанцелярские пинадлежности - ')
print(kans.title, kans.draw())
pen = Pen('\033[34mРучка')
print(pen.title, pen.draw())
pencil = Pencil('\033[35mКарандаш')
print(pencil.title, pencil.draw())
handle = Handle('\033[36mМаркеры')
print(handle.title, handle.draw())