nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for lst in nested_list:
    for val in lst:
        print(val)

[[print(val) for val in lst] for lst in nested_list]

board = [[num for num in range(1,4)]for val in range(1, 4)]
print(board)