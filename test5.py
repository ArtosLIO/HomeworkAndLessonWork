# import sys

# string = sys.argv
# print(string)

# def lowString(up_string: str):
# 	return up_string.lower()

# def upString(low_string: str):
# 	return low_string.upper()


# for l in list(map(lowString, string[1:])):
# 	print(l)

# for l in list(map(upString, string[1:])):
# 	print(l)



# import sys

# string = sys.argv[1:]
# string = list(map(int, string))

# num_simple = []

# for num in string:
# 	i = 2
# 	simple = True
# 	while(i < num):
# 		if not num % i:
# 			simple = False
# 		i += 1
# 	if simple:
# 		num_simple.append(num)

# def square(num: int):
# 	return num ** 2

# list_square = list(map(square, num_simple))
# for l in list_square:
# 	print(l, end=' ')


import sys

name_file = sys.argv[1]
file = open(name_file, 'r')
text_file = file.read().lower().split()
keyword = {}

def recording(w):
	if w in keyword:
		keyword[w] += 1
	else:
		keyword[w] = 1

list(map(recording, text_file))
print(keyword)

file.close()


# for f in file:
# 	if f.split():
# 		f = f.split()
# 		f = [s.lower() for s in f]
# 		for word in f:
# 			if word in keyword:
# 				keyword[word] += 1
# 			else:
# 				keyword[word] = 1
# for k in keyword:
# 	if keyword[k] > 1:
# 		print(k, keyword[k])
# file.close()






