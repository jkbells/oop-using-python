# Access parent class overridden methods

class rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
        def area(self):
            return self.length * self.width
        
        def perimeter(self):
            return 2*self.length + 2*self.width
        
        def __str__(self):
            return "L:" +str (self.length) + "w:" + str(self.width)
            
            
            rect = rectangle(2,4)
            print(rect)
            
            # Here we declare that the square class inherites from the rectangle class

class square(rectangle):
    def __init__(self,length):
        super().__init__(length,length)
        
        def __str__(self):
            return "square:" +super().__str__()
            
square = square(4)
square.area()

print(square)
