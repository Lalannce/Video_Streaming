import re
import csv
import os
import pandas as pd
import numpy as np
import math
import sys
import glob
for input_file_path in glob.glob('/home/lalan/Desktop/MPD/ServerLog/CWND/Result/Cubic/BW/Throu/500/*'):
    pts = '00:00:00'
    pcwnd = '0'
    cts = '00:00:00'
    cwnd_file_path = '/home/lalan/Desktop/MPD/ServerLog/CWND/Result/BBRv2/Packet_Loss/1%/Test/BBRv2_Bola_1_1_out.txt'
    csv_file_path = '/home/lalan/Desktop/MPD/ServerLog/CWND/Result/BBRv2/Packet_Loss/1%/Test/BBRv2_Bola_1_1_cwnd.csv'
    with open(input_file_path, 'r') as file, open(cwnd_file_path, 'w') as output_file, open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Congestion"])
        #print(file)
        for line in file:
            if not line.strip():
                continue
            first_word = line.strip().split()[0]
            if first_word in ['The']:
                words = line.split()
                cts = words[-2]
                continue
            if "2024" in line.strip().split()[-1]:
                continue
            if first_word in ['Cubic;', 'Incoming']:
                output_file.write(line.strip() + '\n')
                numbers = ''.join(char for char in line if char.isdigit())
                if numbers == pcwnd and cts == pts and cts != '00:00:00':
                    continue
                else:
                    csv_writer.writerow([numbers])
                    pcwnd = numbers
                    pts = cts
        df1 = pd.read_csv(csv_file_path)
        df = df1['Congestion']
        print("Minimum Value: ", df.min(), "\nMaximum Value: ",df.max(), "\nAverage value: ",df.mean(), "\nAverage value in kb: ",(df.mean())/1024, "\nMedian value: ",df.median())
    os.remove(csv_file_path)
    os.remove(cwnd_file_path)





# import pandas as pd

# # Specify the path to the CSV file
# file_path = '/home/lalan/Desktop/MPD/ServerLog/CWND/Result/1%/Bola/BBR_Bola_1_1_cwnd.csv'

# # Read the CSV file into a DataFrame
# df = pd.read_csv(file_path)

# # Convert DataFrame values to a flat list of integers
# data_list = df.values.flatten().astype(int).tolist()
# # Print the resulting list
# print("Flat list from CSV file with integers:")
# print(data_list)
