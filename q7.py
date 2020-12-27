m = 50
n = 57

# with open("input_coordinates_7_1.txt", "r") as f:
#     #skip the first line
#     next(f)

#     # for each line
#     for line in f:
#         line = line.strip("\n")
#         coordinates = line.split("\t")
#         for i in range(len(coordinates)):
#             coordinates[i] = int(coordinates[i])
#         print(coordinates)

#         x = coordinates[0]
#         y = coordinates[1]
        

#         index_result = m*y + x

#         with open('output_index_7_1.txt', 'a') as j:
#             j.write(str(index_result) + '\n')

with open("input_index_7_1.txt", "r") as f:
    #skip the first line
    next(f)

    # for each line
    for line in f:
        line = line.strip("\n")
        
        
        target_index = int(line)
        
        coordinate_result_x = (target_index % m)
        coordinate_result_y = int(target_index/m)
        
        with open('output_coordinates_7_1.txt', 'a') as j:
            j.write("{}\t{}".format(coordinate_result_x,coordinate_result_y) + '\n')


