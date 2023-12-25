import pandas as pd
import numpy as np
import csv
import math
from math import log
import glob
total = 0
flag = 0
row = 0
curr_bitrate = 0
prev_bitrate = 0
count = 0
N = -1
Z = 0
BL = 0
pre_val = -1
QoE = []
first = 0
second = 0
third = 0
four = 0
five = 0
avg = 1
i=0
BT = []  # Buffer Time
TotalAB = [] # Total average bitrate
#file_name = 'BBRv2_1000_200.csv'
#value change 9000 to 6600
for file_name in glob.glob('/media/lalan/StudyMaterial/WorkingD/Result/SA/Bola/PacketLoss/5%/*'):
    #print(file_name)
    pre_val = -1
    val = 0
    i=i+1
    if i == 6:
        avg = avg+1
        i=1
    # print(file_name[:-16], end='')
    ########## Delete Redundant Row  #############
    df = pd.read_csv(file_name, index_col=0) # Remove redundant data
    with open(file_name, 'r') as file:
        flag = 0
        row = 0
        data = csv.reader(file)
        for lines in data:
            if flag == 0:
                flag = 1
                continue
            if float(lines[6]) > 0:
                break
            if float(lines[6]) == 0:
                row = row + 1
    df = df.iloc[row:]
    df_new = df[df.videoBitrate != 0]
    df_new.to_csv(file_name, index=True)
    file.close()

    def del_row():
        Z=0
        f=0
        BL = 0
        with open(file_name, 'r') as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                if f == 0:
                    f=1
                    continue
                if float(lines[6]) > 0:
                    BL = int(float(lines[6])*10)                
                if float(lines[6]) == 0:
                    if BL <= 0 :
                        Z = Z+1
                    else:
                        BL = BL - 0.1
        file.close()
        #print(Z)
        return Z


    while True:
        val = del_row()
        #print(len(df))
        #print(val)
        lrow = (-1)*(len(df_new)-9000-val)
        #print(lrow)
        if lrow >= 0:
            break
        df_new = df_new.iloc[:lrow]
        df_new.to_csv(file_name, index=True)
        if val == 0 or pre_val == val:
            break
        pre_val = val
        val = 0
    #print(len(df_new))
    ############## Calculate QoE ####################
    with open(file_name, 'r') as file: # calculate QoE
        csvFile = csv.reader(file)
        flag = 0
        BL = 0
        N = 0
        AB=[]
        count = 0
        for lines in csvFile:
            N = N+1
            if flag == 0:
                flag = 1
                continue
            if float(lines[6]) > 0:
                BL = int(float(lines[6])*10)
            if flag == 1:
                prev_bitrate = float(lines[1])
                flag = 2
                AB.append(int(lines[1]))            
            if flag == 2:
                curr_bitrate = float(lines[1])
                if float(lines[6]) == 0:
                    if BL <= 0 :
                        count = count+1
                    else:
                        BL = BL - 0.1
                        AB.append(int(lines[1]))                 
                total = total + log(curr_bitrate/350) - abs(log(curr_bitrate/prev_bitrate))
                prev_bitrate = curr_bitrate
        total = (total/N) - count*0.266
        #print("{:f}".format(total), count)
        #print(count)
        avg = sum(AB)/len(AB) 
        TotalAB.append(avg)
        QoE.append(total)
        BT.append(count)
    file.close()
print(QoE)
#print(N)
res = np.std(QoE)
#print("Error", res)
print("mean of QoE", np.mean(QoE))
print("Buffer Time", BT)
print("Buffer Time", np.mean(BT))
res1 = np.std(BT)
print("Error BT", res1)
print("Mean of bitrate", np.mean(TotalAB))