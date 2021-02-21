class point:
    # constructor are defined using a special method which must be named --init--
    
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        

p1 = point()          # p1 is a reference variable
print ("p1 = ",p1.x)

p2 = point(2,4)           # notice that we do not pass in self that is automatically done for 
print ("p2 = ",p2.x)


print(p2)
