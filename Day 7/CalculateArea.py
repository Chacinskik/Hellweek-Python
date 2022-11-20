import math


class CalculateArea:
    
    def triangle(a: float, h: float) -> float:
        try:
            return (a*h)/2
        except TypeError:
            print("Incorrect method arguments.")
            return None
            
    
    def square(a: float) -> float:
        try:
            return a**2
        except TypeError:
            print("Incorrect method arguments.")
            return None

    def trapeze(a: float, b: float, h: float) -> float:
        try:
            return ((a+b)*h)/2
        except TypeError:
            print("Incorrect method arguments.")
            return None
    
    def circle(r: float) -> float:
        try:
            return math.pi*(r**2)
        except TypeError:
            print("Incorrect method arguments.")
            return None