bd_file = open('bd.txt', 'r') 
file_read = {}


def LerningTwoAndMoreCourse():
	for name in file_read:
		length = len(file_read[name][-1].split(', '))
		if length > 1:
			print(f"{name} учиться на {length} курсах: {file_read[name][-1]}")
	print()

def LerningFrontEnd():
	for name in file_read:
		cours = file_read[name][-1].split(', ')
		if 'FrontEnd' not in cours:
			print(f"{name} не учиться на FrontEnd")
	print()

def LerningPythonOrJava():
	for name in file_read:
		cours = file_read[name][-1].split(', ')
		if 'Python' in cours or 'Java' in cours:
			print(f"{name} изучает Python или Java")
	print()


for f in bd_file:
	f = f.split(': ')
	f[1], f[2] = list(map(int, f[1].split(', '))), f[2].strip('\n')
	f[1].append(f[2])
	file_read[f[0]] = f[1]

max_val = ['', 0]
min_val = ['', 100]
for name in file_read:
	mean_value = (name, sum(file_read[name][:-1]) / len(file_read[name][:-1]))
	if mean_value[1] > max_val[1]:
		max_val[0] = mean_value[0]
		max_val[1] = mean_value[1]
	if mean_value[1] < min_val[1]:
		min_val[0] = mean_value[0]
		min_val[1] = mean_value[1]

print(f"Успешный ученик {max_val[0]}: {max_val[1]}")
print(f"Отстающий ученик {min_val[0]}: {min_val[1]}", end='\n\n')

LerningTwoAndMoreCourse()
LerningFrontEnd()
LerningPythonOrJava()



# size = {
# 	'XXS': {'Russia': 42, 'Germany': 36, 'USA': 8, 'France': 38, 'United Kingdom': 24},
# 	'XS': {'Russia': 44, 'Germany': 38, 'USA': 10, 'France': 40, 'United Kingdom': 26},
# 	'S': {'Russia': 46, 'Germany': 40, 'USA': 12, 'France': 42, 'United Kingdom': 28},
# 	'M': {'Russia': 48, 'Germany': 42, 'USA': 14, 'France': 44, 'United Kingdom': 30},
# 	'L': {'Russia': 50, 'Germany': 44, 'USA': 16, 'France': 46, 'United Kingdom': 32},
# 	'XL': {'Russia': 52, 'Germany': 46, 'USA': 18, 'France': 48, 'United Kingdom': 34},
# 	'XXL': {'Russia': 54, 'Germany': 58, 'USA': 20, 'France': 50, 'United Kingdom': 36},
# 	'XXXL': {'Russia': 56, 'Germany': 60, 'USA': 22, 'France': 52, 'United Kingdom': 38}
# }

# input_size = input("Enter size your clothes: ").upper()

# if input_size in size.keys():
# 	for country in size[input_size]:
# 		print(f"Size on {country}: {size[input_size][country]}")















