data = [5, "Python", 3.14, -2, "Data", True, 0, 12.5, 9, "AI", None, 4]
integer = filter(lambda x: type(x) == int, data)
integer = list(integer)

squares = map(lambda x: x**2, integer)
squares = list(squares)

print(integer)
print(squares)
