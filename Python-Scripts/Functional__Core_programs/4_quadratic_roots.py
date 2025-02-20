import math

def calculate_delta(a: int, b: int, c: int) -> int:
    delta = (b * b) - (4 * a * c)
    return delta

def calculate_roots(a: int, b: int, delta: int) -> float:
    if delta < 0:
        return "No Real Roots" 

    root1 = (-b + math.sqrt(delta)) / (2 * a)
    root2 = (-b - math.sqrt(delta)) / (2 * a)

    return root1, root2

a = int(input("Enter coefficient of a: "))
b = int(input("Enter coefficient of b: "))
c = int(input("Enter coefficient of c: "))

delta = calculate_delta(a , b , c)
roots = calculate_roots(a , b , delta)

print("Delta: ", delta)
print("Roots: ", roots)