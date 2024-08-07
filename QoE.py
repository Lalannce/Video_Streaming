import glob
import numpy as np
import pandas as pd

def calculate(fname):
    df=pd.read_csv(fname)
    df=df[~(df.videoBufferLength==0).cumprod().astype("bool")]
    arr=df.videoBufferLength.values
    for i in range(1,len(arr)):
        if arr[i]==0 and arr[i-1]>=0.1:
            arr[i]=arr[i-1]-0.1
    df['videoBufferLength']=arr
    print(fname)
    print(df.shape,df[~(df.videoBufferLength==0)].shape)
    if df[~(df.videoBufferLength==0)].shape[0]<9000:
        take=df[~(df.videoBufferLength==0)].shape[0]
    else:
        take=9000
    df=df.loc[:df[~(df.videoBufferLength==0)].reset_index().iloc[take-1]['index']]
    f_df=df[df.videoBufferLength>0]

    #Calculate QoE, BuffTime, BitRate
    buffTime=(df.videoBufferLength==0).sum()/10 #second

    bitRate=f_df.videoBitrate.mean()
     # f_df.videoBitrate.min()
#     print(df.shape,df.videoBitrate.max(),df.videoBitrate.min(),np.log10(df.videoBitrate/df.videoBitrate.min()).sum())

    QoE=\
    np.log10(f_df.videoBitrate/200).sum()-\
    2.66*buffTime-\
    np.abs(np.log10(df.videoBitrate.values[1:])-np.log10(df.videoBitrate.values[:-1])).sum()
    diff=np.abs(np.log10(df.videoBitrate.values[1:])-np.log10(df.videoBitrate.values[:-1])).sum()
    return [fname,buffTime, bitRate, QoE, diff]
#/media/lalan/StudyMaterial/WorkingD/Result/SA/Test/VS_Data/PacketLoss/Throughput/Reno/5%
#/media/lalan/StudyMaterial/WorkingD/Result/SA/VideoStreamingLog/SERVER_LOG/Throu/Reno/Packet Loss/5%
files=glob.glob("/media/lalan/StudyMaterial/WorkingD/Result/SA/Test/VS_Data/PacketLoss/Throughput/BBR/3%/*")

stat=[]
for f in files:
    stat.append(calculate(f))

df_stat=pd.DataFrame(stat,columns=['fname','buffTime','bitRate','QoE','Diff'])
print(df_stat)
print(df_stat.drop(columns=['fname']).mean())
