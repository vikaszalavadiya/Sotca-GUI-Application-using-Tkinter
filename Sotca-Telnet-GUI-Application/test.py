import telnetlib
import asyncio, telnetlib3
import getpass
import os
import sys
import time
import socket

#tn = telnetlib3.open_connection('192.168.1.100', 10001)

#outp = reader.read(1024)


ip1 ="192.168.1.100"
port1 = 10001
timeout1 = 5

tn = telnetlib.Telnet(ip1, port1, timeout1)

w1 = "{01CA1}"

tn.write(str.encode(w1, 'UTF-8'))

# while True:
# 	result = 0
# 	#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 	#sock.settimeout(2)  # 2 Second Timeout
# 	#result = sock.connect_ex((ip1, port1))
# 	#sock.close()
# 	if result == 0:
# 		#print('port OPEN')
#
#
# 		d1 = "{01M1}"
# 		d1 = str.encode(d1, 'UTF-8')
# 		tn.write(d1)
# 		time.sleep(0.5)
# 		read = tn.read_some()
# 		print(read)
# 		read2 = bytes([(p, 00)[p == 0xff] for p in read])
# 		read2 = read2.decode('UTF-8')
# 		print(read2)
# 		tn.close()
# 		#time.sleep(0.5)
# 	else:
# 		print('port CLOSED, connect_ex returned: ' + str(result))
