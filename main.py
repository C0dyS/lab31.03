class Area_calculator:
    _amount_of_uses = 0
    @staticmethod
    def right_angled_triangle_area(b,h):
        Area_calculator._amount_of_uses += 1
        return (1/2)*b*h
    @staticmethod
    def isosceles_triangle_area(a,b):
        Area_calculator._amount_of_uses += 1
        return (1/4)*b*((4*a**2)-b**2)**(1/2)
    @staticmethod
    def equilateral_triangle_area(a):
        Area_calculator._amount_of_uses += 1
        return (3/(4*a**2))**(1/2)
    @staticmethod
    def rectangle_area(a):
        Area_calculator._amount_of_uses += 1
        return a**2
    @staticmethod
    def romb_area(d_1,d_2):
        Area_calculator._amount_of_uses +=1
        return d_1*d_2/2
    @staticmethod
    def get_amount_of_uses():
        return Area_calculator._amount_of_uses

print(Area_calculator.romb_area(1,3))
print(Area_calculator.get_amount_of_uses())
print(Area_calculator.romb_area(1,3))
print(Area_calculator.get_amount_of_uses())
print(Area_calculator.romb_area(1,3))
print(Area_calculator.get_amount_of_uses())



