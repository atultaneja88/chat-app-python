import socket 
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
s.bind(("127.0.0.1",8000))
s.listen(5)
conn,addr= s.accept()
print("got connection from",addr)
while True:
    conn.send(bytes("atul=>"+input(),encoding='utf-8'))
    print(conn.recv(1024))