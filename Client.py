import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
port=9999
s.connect((host,port))
message = input("Enter the message :")
s.send(bytes(message,"utf-8"))
print("Message from server",s.recv(1024).decode("utf-8"))
s.close()