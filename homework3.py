from random import randint

file = open('raund.txt', 'w') # clear file and write in file random number
for i in range(1, 21):
	fizz = randint(1, 10)
	buzz = randint(11, 20)
	count = randint(21, 40)
	file.write(f"{fizz} {buzz} {count}\n")
	print(f"{fizz} {buzz} {count}")
file.close()

f = open("conclusion_list.txt", 'w') # clear file
file = open('raund.txt', 'r')

for line in file:
	line = line.split()
	fizz = int(line[0])
	buzz = int(line[1])
	count = int(line[2])

	for i in range(1, count+1):
		if (i % fizz) == 0 and (i % buzz) == 0:
			print("FB", end=' ')
			f.write("FB ")
		elif (i % fizz) == 0:
			print("F", end=' ')
			f.write("F ")
		elif (i % buzz) == 0:
			print("B", end=' ')
			f.write("B ")
		else:
			print(i, end=' ')
			f.write(f"{i} ")
	f.write("\n")
	print()

file.close()