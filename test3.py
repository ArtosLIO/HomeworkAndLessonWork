# c = {1:'a', 2:'b', 3:'c'}
# c = "qwertyu"
# for i in enumerate(c):
# 	print(i[1])

# line = (4, 23, 48, 84, 79, 85, 35, 67)
# summa = 0
# for i in line:
# 	summa += i
# print(summa)
# i = 0
# while i < len(line):
# 	summa += line[i]
# 	i += 1
# print(summa)


# import sys
# filename = sys.argv[1]
# f = open(filename, 'r')
# for line in f:
# 	print(line, end='')


# import sys
# filename = sys.argv[1]
# f = open(filename, 'r')
# text = []
# for line in f:
# 	text.append(line)
# count = len(text)
# while count >= 0:
# 	count -= 1
# 	print(text[count], end='')
# f.close()


# import sys
# money = int(sys.argv[1])
# list_bank = (1000, 500, 200, 100, 50, 20, 10, 5, 2, 1)
# for l in list_bank:
# 	i = 0
# 	while money >= l:
# 		i += 1
# 		money = money - l
# 		if money < l:
# 			print("Quantity {} bills {}".format(l, i))


# import sys
# money_list = sys.argv[1]
# hang = 0
# i = 0
# list_bank = (10, 20, 50, 100, 200, 500)

# for l in money_list[::-1]:
# 	l = int(l)
# 	while l > list_bank[hang] and i < 10 and hang != 6:
# 		l -= 1
# 		i += 1
# 		if l == 0:
# 			print("Quantity {} bills {}".format(list_bank[hang], i))
# 	if hang == 6:
# 		money = int(money_list)//1000
# 		while money != 0:
# 			money -= 1
# 			i += 1
# 			if money == 0:
# 				print("Quantity 1000 bills {}".format(i))
# 	if hang == 6:
# 		break
# 	hang += 1
# 	i = 0


import sys
money_list = sys.argv[1]
money = int(money_list)
hang = 0
i = j = 0
list_bank = (10, 20, 50, 100, 200, 500)
money = int(money_list)

while True:
	while i < 10 and hang < 3 and money >= list_bank[hang]:
		if money > list_bank[hang] and int(money_list[-2]) > 0:
			i += 1
			money -= list_bank[hang]
			money_list = str(money)
			if int(money_list[-2]) == 0 or i == 10 or money < list_bank[hang]:
				print("Quantity {} bills {}".format(list_bank[hang], i))
				break
		elif money >= list_bank[hang] * 10 and not i:
			money -= list_bank[hang] * 10
			money_list = str(money)
			print("Quantity {} bills 10".format(list_bank[hang]))
			break
		elif money >= list_bank[hang]:
			i += 1
			money -= list_bank[hang]
			money_list = str(money)
			if i == 10 or money < list_bank[hang]:
				print("Quantity {} bills {}".format(list_bank[hang], i))
				break
		else:
			break
		
	while i < 10 and 2 < hang < 6 and money >= list_bank[hang]:
		if money > list_bank[hang] and int(money_list[-3]) > 0:
			i += 1
			money -= list_bank[hang]
			money_list = str(money)
			if int(money_list[-3]) == 0 or i == 10 or money < list_bank[hang]:
				print("Quantity {} bills {}".format(list_bank[hang], i))
				break
		elif money >= list_bank[hang] * 10 and not i:
			money -= list_bank[hang] * 10
			money_list = str(money)
			print("Quantity {} bills 10".format(list_bank[hang]))
			break
		elif money >= list_bank[hang]:
			i += 1
			money -= list_bank[hang]
			money_list = str(money)
			if i == 10 or money < list_bank[hang]:
				print("Quantity {} bills {}".format(list_bank[hang], i))
				break
		else:
			break

	if hang == 6:
		while money >= 1000:
			money -= 1000
			money_list = str(money)
			i += 1
			if money == 0:
				print("Quantity 1000 bills {}".format(i))
				break

	print(money)
	if hang >= 6:
		break
	if i or j:
		i = 0
		j = 0
	hang += 1
	if not money:
		break









