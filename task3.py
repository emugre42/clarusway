data = [5, "Python", 3.14, -2, "Data", True, 0, 12.5, 9, "AI", None, 4]

integers = [ i**2 for i in data if type(i) == int ]
integers

squares = []

for i in integers:
    squares.append(i)

print(squares)
