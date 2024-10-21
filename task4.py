data = [5, "Python", 3.14, -2, "Data", True, 0, 12.5, 9, "AI", None, 4]

integer_filter = [ i if type(i) == int else None for i in data ]
integer_filter

integer_squares = []

for i in integer_filter:
    if type(i) == int:
        i = i**2
        integer_squares.append(i)
    else:
        integer_squares.append(None)
        
print(integer_squares)
