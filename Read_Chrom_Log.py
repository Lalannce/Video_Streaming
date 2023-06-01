import json
import pandas as pd

stack=[]
f=open("out3.har","r")

for i in range(9):f.readline() #dump

def process_brackets(line):
    for e in line:
        if e=='{'or e=='[':
            stack.append(e)
        elif e=='}':
            if stack[-1]=='{':
                stack.pop()
            else:
               stack.append(e)
        elif e==']':
            if stack[-1]=='[':
                stack.pop()
            else:
               stack.append(e)
data=[]
while True:
    curr_chunk=line=f.readline()
    try:
        process_brackets(line)
    except:
        break
    while len(stack)>0:
        line=f.readline()
        process_brackets(line)
        curr_chunk+=line
    try:
        chk=json.loads(curr_chunk[:-2])
    except:
        chk=json.loads(curr_chunk[:-1])
    data.append([chk["response"]["headers"][-1]["value"],
    chk["response"]["content"]["size"],
    chk["response"]["_transferSize"],
    chk["serverIPAddress"],
    chk["startedDateTime"],
    chk["time"],
    *chk["timings"].values()])


df=pd.DataFrame(data,columns=['chunk','content_size','transfer_size','serverIP','starteDateTime','time','blocked', 'dns', 'ssl', 'connect', 'send', 'wait', 'receive', '_blocked_queueing'])
df.to_csv("out3.csv",index=False)

f.close()