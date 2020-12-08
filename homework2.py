val1 = int(input("Enter first value: "))
val2 = int(input("Enter second value: "))

# First task
if val1 < val2:
	print(f"1. {val1} less {val2}")
if val1 > val2:
	print(f"2. {val1} more {val2}")
if val1 == val2:
	print(f"3. {val1} equally {val2}")
if val1 <= 10 and val2 <= 10:
	print(f"4. {val1} and {val2} less or equally 10")
if val1 > 10 or val2 > 10:
	print(f"5. {val1} or {val2} more 10")
if val1 != val2:
	print(f"6. {val1} not equally {val2}")
if val1 is val2:
	print(f"7. {val1} is {val2}")
if 10 not in (val1, val2):
	print(f"8. 10 not in {val1} or {val2}")
print()

# Second task
if val1 == val2:
	print(f"9. Square with sides {val1}.")
elif val1 > 0 and val2 > 0 and (val1 > val2 or val1 < val2):
	print(f"9. Rectangle with sides {val1} and {val2}.")
else:
	print(f"Impossible to build a figure!")


# FizzBuzz
fizz = int(input("Enter first value: "))
buzz = int(input("Enter second value: "))
count = int(input("Enter third value: "))

for i in range(1, count+1):
	if (i % fizz) == 0 and (i % buzz) == 0:
		print("FB", end=' ')
	elif (i % fizz) == 0:
		print("F", end=' ')
	elif (i % buzz) == 0:
		print("B", end=' ')
	else:
		print(i, end=' ')








