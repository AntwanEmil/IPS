import socket

UDP_IP = "138.68.183.168"
UDP_PORT = 5005
MESSAGE = "Hello, World!"

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)
while 1:
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))
