# classes in python

class Animal:
    legs=False
    name=''
    
    def sound(self):
        return '*silence*'
    def move(self):
        return True
        
        a = Animal()
        
        a.legs
        
        a.name
        
        a.sound()
        a.move()
        
        
        
 # this is child class

class dog(Animal):
    def sound(self):
        return 'Bark!'
        
        class cat(Animal):
    def sound(self):
        return 'Meow!!'
        
        d=dog()
        d.sound()
        
        c=cat()
        c.sound()
        
        d.move()
        
        
        
