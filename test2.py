# val = int(input("Enter value: "))
# if val % 2 == 0:
#   print("Even number!")
# else:
#   print("Odd number!")


# val = int(input("Enter value: "))
# if val % 2 != 0 and val % 3 == 0 and val % 5 == 0 and val % 10 != 0:
#   print("All right!")
# else:
#   print("WASTED!")


# val = int(input("Enter value: "))
# for i in range(1, (val+1)):
#   if (val % i) == 0:
#       print(i)


# val = int(input("Enter value: "))
# ed = val % 10
# de = int((val % 100) * 0.1)
# so = int((val % 1000) * 0.01)
# if ed > 0:
#     for i in range(1, (ed + 1)):
#         for k in range(1, (i+1)):
#             if (i * k) == ed:
#                 print("{} * {} = {}".format(i, k, ed))

# if de > 0:
#     for i in range(1, (de + 1)):
#         for k in range(1, (i+1)):
#             if (i * k) == de:
#                 print("{} * {} = {}".format(i, k, de))
                
# if so > 0:
#     for i in range(1, (so + 1)):
#         for k in range(1, (i+1)):
#             if (i * k) == so:
#                 print("{} * {} = {}".format(i, k, so))
                

# string = input("Enter value: ")
# for j in range(1, len(string)+1):
#     val = int(string[-j])
#     if val > 0:
#         for i in range(1, (val + 1)):
#             for k in range(1, (i+1)):
#                 if (i * k) == val:
#                     print("{} * {} = {}".format(i, k, val))


# string = input("Enter value: ")
# val = "{} = ".format(string)
# count = len(string)
# k = 0
# for i in string[::-1]:
#     if k == 0:
#         val += "{}".format(i, k)
#     else:
#         val += "{} * 10^{}".format(i, k)
#     if k < (count - 1):
#         val += " + "
#     k += 1
# print(val)









