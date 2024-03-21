class Human:
    _attribute = 0

    def __init__(self):
        Human._attribute += 1
    @staticmethod
    def check_amount_of_instances():
        return Human._attribute





a = Human()
b = Human()
c = Human()
d = Human()
print(a.check_amount_of_instances())
print(b.check_amount_of_instances())