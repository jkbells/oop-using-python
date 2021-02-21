# composition

class shape:
    def __init__(self,points):
        self.points = points
        
    def __str__(self):
        ret = ""
        for i in self.points:
            ret += str(i) + "-"
            return ret
            
p1 = point(5,5)
p2 = point(10,5)
p3 = point(5,10)
p = [p1,p2,p3]

sh = shape(p)

# we can add methods to calss even after it has been defined
print (sh)


def print_points(self):
    for i in self.points:
        print(i)
        shape.print_points = print_points
        
        
        sh.print_points()
