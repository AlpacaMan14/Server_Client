import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
port=9999
s.bind((host,port))
print ("Waiting for connection...")
s.listen(5)
while True:
    conn,addr=s.accept()    
    print ('Got connection from',addr)
    message=conn.recv(1024).decode("utf-8")[::-1]
    conn.send(bytes(message,"utf-8"))
    conn.close()