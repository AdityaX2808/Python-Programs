def euclidian_distance(x : int , y : int) -> float:
    distance = ((x * x) / (y * y)) ** 0.5
    return distance

x = int(input("Enter the coordinates of x: "))
y = int(input("Enter the coordinates of y: "))

distance_x_and_y = euclidian_distance(x , y)

print(distance_x_and_y)