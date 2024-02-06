inv_pyramid = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(inv_pyramid), 0, -1):
    spaces = ' ' * (len(inv_pyramid) - i)
    print(spaces + str(inv_pyramid[:i]))
