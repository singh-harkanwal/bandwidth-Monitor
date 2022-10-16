#Bandwidth Monitor program using psutil library
#This will provide the number of bytes and packets exchanged per second

import time
import psutil
from datetime import datetime

#Get system-wide network input/output statistics
previous_net_counters = psutil.net_io_counters()

#Bytes received in the previous second
previous_received_bytes = previous_net_counters.bytes_recv
#Bytes sent in the previous second
previous_sent_bytes = previous_net_counters.bytes_sent
#Total bytes exchanged in the previous second
previous_total_bytes = previous_received_bytes + previous_sent_bytes

#Packets received in the previous second
previous_received_packets = previous_net_counters.packets_recv
#Packets sent in the previous second
previous_sent_packets = previous_net_counters.packets_sent

#This endless loop will count the current bytes and packets 
#and print the difference as compared to the last second 
while True: 
    #Get system-wide network input/output statistics
    current_net_counters = psutil.net_io_counters()
    
    #Current bytes received    
    current_received_bytes = current_net_counters.bytes_recv
    #Current bytes sent
    current_sent_bytes = current_net_counters.bytes_sent
    #Current total bytes exchanged
    current_total_bytes = current_received_bytes + current_sent_bytes
    
    #Current packets received
    current_received_packets = current_net_counters.packets_recv
    #Current packets sent
    current_sent_packets = current_net_counters.packets_sent
    
    #Bytes received in the last second
    bytes_received_in_last_sec = current_received_bytes - previous_received_bytes
    #Bytes sent in last the second
    bytes_sent_in_last_sec = current_sent_bytes - previous_sent_bytes
    #Total bytes exchanged in the last second
    total_bytes_in_last_sec = current_total_bytes - previous_total_bytes
    
    #Packets received in last second
    packets_received_in_last_sec = current_received_packets - previous_received_packets
    #Packets sent in last second
    packets_sent_in_last_sec = current_sent_packets - previous_sent_packets
    
    #Current time to print
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    #Convert bytes into MB and print the information   
    print(f"{current_time}: {bytes_received_in_last_sec / 1024 / 1024:.2f} MB received, {bytes_received_in_last_sec / 1024 / 1024:.2f} MB sent, total {total_bytes_in_last_sec / 1024 / 1024:.2f} MB exchanged | Packets: {packets_received_in_last_sec} received, {packets_sent_in_last_sec} sent")
    
    #Assign all the current values to the previous values     
    previous_received_bytes = current_received_bytes
    previous_sent_bytes = current_sent_bytes
    previous_total_bytes = current_total_bytes
    
    previous_received_packets = current_received_packets
    previous_sent_packets = current_sent_packets
    
    #Set the time difference to 1 second
    time.sleep(1)