import csv
from random import randrange

headers = ['x_accel', 'y_accel', 'z_accel', 'Class']

# Creates an excel file with 101 rows x 3 columns of random x,y,z accelerometer data from 100-300
with open('Sample_Acc_Data.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(headers)

    for _ in range(100):
        some_lst = []
        for _ in range(3):
            some_lst.append(randrange(100, 300))
        some_lst.append(randrange(3))
        csv_writer.writerow(some_lst)
