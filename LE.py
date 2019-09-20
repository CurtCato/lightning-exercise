# LE: 8/28/2019
Appliances = ('oven', 'refrigerator', 'coffee maker', 'rice cooker')

Appliances = Appliances + ("blender", "ice cream maker", "microwave")

print(Appliances)

# LE: 9/3/2019
class Boat():

    def __init__(self, type, speed):
        self.type = type
        self.speed = speed

    def move(self, speed):
        return f"This Boat moves at {speed} knots."


class Kayak(Boat):

    def __init__(self, passengers=1):
        super().__init__("kayak", "paddle")
        self.passengers = passengers

    def paddle(self, speed):
        print(f"I like to go out in my Kayak and {self.move(speed)}")

padde_kayak = Kayak()
padde_kayak.paddle(7)
print(padde_kayak.move(5))

# LE: 9/4/2019

# 1. write a function called add that accepts two arguments and returns their sum
# 1. write a function called subtract that accepts two arguments and returns the difference
# 1. write a function called calculate that accepts a function as an argument. In calculate's body, it should execute that function and pass it the numbers 3 and 5
# 1. print an execution of calculate and pass it a reference to add
# 1. print an execution of calculate and pass it a reference to subtract

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def calculate(function):
    print(function(3,5))

calculate(add)

calculate(subtract)


