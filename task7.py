age = int(input("Enter your age: "))

output = "Welcome, and Have fun!" if age >= 18 else "Please scan your parent's ID first" if age < 18 and age >= 16 else "Return to your home!"

print(output)
