class Quadratic:
    def __init__(self,a, b, c):
        self.a = a
        self.b = b
        self.c = c
        # Checks and calculates value for square roots accordingly
        for i in range(0,3):
            n = input("Is a value square root (y/n)? ")
            if n == 'y':
                val = input("Which value (a,b,c)? ")
                if val == 'a':
                    self.a = self.a**0.5
                    print(self.a)

                elif val == 'b':
                    self.b = self.b**0.5
                    print(self.b)

                elif val == 'c':
                    self.c = self.c**0.5
                    print(self.c)
            elif(n=='n'):
                break

    # Finds the Discriminant of the root
    def Discriminant(self):
        self.d = pow((self.b),2) - 4*self.a*self.c  
        print(self.d)

        if self.d == 0: # Compares value of discriminant to check nature of the roots
            print("The quadratic has two similar roots")
            print(f"The discriminant of the given quadratic is {self.d}")
        elif self.d <= 0:
            print("The quadratic has no real/imaginary roots")
            self.d = complex(0, -self.d)
            print(f"The discriminant of the given quadratic is {self.d}")
        elif self.d >= 0:
            print("The quadratic has two disimilar roots")
            print(f"The discriminant of the given quadratic is {self.d}")

        return self.d 
    
    # Solves for the values of the quadratic formula
    def Sol(self):
        
        self.d = self.d**0.5
        
        self.r1 = (-self.b + self.d)/2*self.a
        print(f"Root 1 of the given quadratic is {self.r1}")
        
        self.r2 = (-self.b - self.d)/2*self.a
        print(f"Root 2 of the given quadratic is {self.r2}")

print("Enter all the values (Don't include any symbols, mathematical operators, functions etc)")

p = int(input("Coefficient of x^2: "))
q = int(input("Coefficient of x: "))
r = int(input("Constant term: "))
    
Quad = Quadratic(p,q,r)
Quad.Discriminant()
Quad.Sol()
