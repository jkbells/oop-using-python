# Multiple inheritance

class triangle(shape):   # triangle inheritis from shape
    pass                 # pass means im not going to have anything in this block
    
    t = triangle(p)
    
    t.print_pointS()  # automatically inherited
    
    def get_area(self):
    vertices = self.points
    n= len(vertices)   # of corners
    a = 0.0
    for i in range(n):
        j = (i+1)%n
        a += abs(vertices[i].x*vertices[j].y-vertices[j].x*vertices[i].y)
        return a/2.0
    triangle.get_area = get_area
    
    
    t.get_area()
    
    
    
    
