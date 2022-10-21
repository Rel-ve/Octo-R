class Quadratic:
    def __init__(self,a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def Discriminant(self):
        self.d = pow((self.b),2) - 4*self.a*self.c # Finds the Discriminant of the root 
        print(self.d)

        if self.d == 0: # Compares value of discriminant to check nature of the roots
            print("The quadratic has two similar roots")
            print(f"The discriminant of the given quadratic is {self.d}")
        elif self.d <= 0:
            print("The quadratic has no/imaginary roots")
            self.d = complex(0, -self.d)
            print(f"The discriminant of the given quadratic is {self.d}")
        elif self.d >= 0:
            print("The quadratic has two disimilar roots")
            print(f"The discriminant of the given quadratic is {self.d}")

        return self.d 

    def Sol(self):
        
        self.d = self.d**0.5
        
        self.r1 = (-self.b + self.d)/2*self.a
        print(f"Root 1 of the given quadratic is {self.r1}")
        
        self.r2 = (-self.b - self.d)/2*self.a
        print(f"Root 2 of the given quadratic is {self.r2}")

p = int(input("Coefficient of x^2: "))
q = int(input("Coefficient of x: "))
r = int(input("Constant term: "))

Quad = Quadratic(p,q,r)
Quad.Discriminant()
Quad.Sol()
