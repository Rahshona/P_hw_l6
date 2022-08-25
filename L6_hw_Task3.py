class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return 'with wage' + ' ' + self._income.get('wage') + ' ' + "and bonus" + ' ' + self._income.get('bonus')

staff = Position('Sara', 'McSomally', 'scientist', '50000', '60000' )
print(staff.get_full_name(), staff.position, staff.get_total_income())
