import dpkt
import datetime
counter=0
ipcounter=0
tcpcounter=0
udpcounter=0

filename='myTrace.pcap0
#f = open(filename)
flag = 0
prev_time = datetime.datetime.now()
for ts, pkt in dpkt.pcap.Reader(open(filename,'r')):
    if flag == 0:
        prev_time = datetime.datetime.utcfromtimestamp(ts)
        #new_time = datetime.datetime.utcfromtimestamp(ts)
        flag = 1
    new_time = datetime.datetime.utcfromtimestamp(ts)
    #print ('Delay: ', (new_time-prev_time).total_seconds()*1000)
    print (int((new_time-prev_time).total_seconds()*1000))
    #print('Timestamp: ', str(datetime.datetime.utcfromtimestamp(ts)))

    counter+=1
    eth=dpkt.ethernet.Ethernet(pkt) 
    if eth.type!=dpkt.ethernet.ETH_TYPE_IP:
       continue

    ip=eth.data
    ipcounter+=1

    if ip.p==dpkt.ip.IP_PROTO_TCP: 
       tcpcounter+=1

    if ip.p==dpkt.ip.IP_PROTO_UDP:
       udpcounter+=1
    #prev_time = new_time

print("Total number of packets in the pcap file: ", counter)
print("Total number of ip packets: ", ipcounter)
print("Total number of tcp packets: ", tcpcounter)
print("Total number of udp packets: ", udpcounter)
