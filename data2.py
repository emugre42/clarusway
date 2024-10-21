data = [5, "Python", 3.14, -2, "Data", True, 0, 12.5, 9, "AI", None, 4]

integer_or_not = map(lambda x: x if type(x) == int else None, data)
integer_or_not = list(integer_or_not)

squares_for_integers = map(lambda x: x**2 if type(x) == int else None, data)
squares_for_integers = list(squares_for_integers)

print(integer_or_not)
print(squares_for_integers)
