print("Enter all the values(if in fraction form, type f, otherwise type anything)")

class Quadratic():
    def __init__(self):
        # Checks if user wants to provide fractional value, if f is stored, input is taken for the fractional values
        choice = input("")
        if choice == 'f':
            for i in range(0,3):
                n = input("Which fractional value does each function have (if a number is integer, put Denominator as 1) ")
                
                if n == 'a':
                    print("Input both values")
                    x = int(input("Numerator: "))
                    y = int(input("Denominator: "))
                    self.a = x/y
                    print(f"Coefficient of x^2 is {self.a}")

                elif n == 'b':
                    print("Input both values")
                    x = int(input("Numerator: "))
                    y = int(input("Denominator: "))
                    self.b = x/y
                    print(f"Coefficient of x is {self.b}")

                elif n == 'c':
                    print("Input both values")
                    x = int(input("Numerator: "))
                    y = int(input("Denominator: "))
                    self.c = x/y
                    print(f"Constant term is {self.c}")
                else:
                    break
        else:
            self.a = int(input("Coefficient of x^2: "))
            self.b = int(input("Coefficient of x: "))
            self.c = int(input("Constant term: ")) 

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
    
Quad = Quadratic()

Quad.Discriminant() # Prints the discriminant of the quadratic formula evaluated in the above class

Quad.Sol() # Prints the two roots of the quadratic
