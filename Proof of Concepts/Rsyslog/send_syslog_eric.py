#Part 1


import socket
import time

def send_syslog(filename, host, protocol):
    #enter my code here
    protocol = protocol.upper()
    if protocol !="TCP" and protocol != "UDP":
        print("Invalid protocol specified")
        return
    
    lines = open(filename, 'r').readlines()

    if protocol == "TCP":
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, 514))
    else:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    for line in lines:
        message = line.strip()
        if protocol == "TCP":
            sock.send((message + '\n'),encode('utf-8'))
        elif protocol == "UDP":
            sock.sendto(message.encode('utf-8'), (host, 514))
        print(f"Sent: {message}")
        time.sleep(1)

send_syslog('system2.log', '127.0.0.1', 'UDP')
