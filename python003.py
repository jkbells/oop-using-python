# inheritance example

class Polygon:
    def __init__(self, no_of_sides):     # called a constructor 
        print ("Creating a polygon of sides: "), no_of_sides
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def set_sides(self, sides):
        self.sides = sides

    def show_sides(self):
        for i in self.sides: 
            print ("Side: "), i
            
            q = Polygon(3)
            
            p = Polygon(4)
            
            q.n

            p.n
            
            

p.show_sides()


q.set_sides([3, 4, 5])
q.show_sides()


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

    def get_area(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s * (s-a)*(s-b)*(s-c)) ** 0.5  # just the formula
        return area
        
        t = Triangle()
t.set_sides([3, 4, 5])

t.show_sides()

t.get_area()




class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 4)
        
    def set_sides(self, sides):  
        assert sides[0] == sides[2], "Opposite sides must be equal"
        assert sides[1] == sides[3], "Opposite sides must be equal"
        self.sides = sides

    def get_area(self):
        area = self.sides[0] * self.sides[1]
        return area



r = Rectangle()

r.set_sides([2, 1, 2, 1])

r.set_sides([2, 5, 2, 7 ])



r.get_area()




