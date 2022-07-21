class complex:
    def __init__(self, a, b):
        self.a = a 
        self.b = b

    
    #adding two objects
    def __add__(self,other):
        return self.a + other.a, self.b + other.b 

Obj1 = complex(1,2) 
Obj2 = complex(2,3)
Obj3 = Obj1 + Obj2

print(Obj3)