import csv
from random import randrange

with open('NewRandom.csv', 'w', newline='') as NewRandom:
    fieldnames = ['accel_x', 'accel_y', 'accel_z', 'class_xyz']
    csv_writer = csv.writer(NewRandom)
    csv_writer.writerow(fieldnames)

    # Dad's Solution
    my_list = []
    list_xyz = []
    for i in range(13):
        my_list.append(randrange(5, 70))

    print(my_list)
    j = 3
    while j < 13:
        new_list = my_list[j-3:j]
        print(new_list)
        new_list.append(randrange(1, 4))
        print(new_list)
        csv_writer.writerow(new_list)

        j += 3

    # Hassan's Solution
    # for i in range(100):
    #     my_list = []
    #     for j in range(3):
    #         my_list.append(randrange(5, 70))
    #     csv_writer.writerow(my_list)
    #     print(my_list)
