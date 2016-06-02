import socket
from present_implementation import PresentCypherImplementation
print "Insert port to listen"
port = int(raw_input())
sock = socket.socket()
host = socket.gethostname()
sock.bind((host, port))
sock.listen(5)
cypher = PresentCypherImplementation()
print "Server listening on port: %d" % port
flag = True

while flag:
    conn, addr = sock.accept()
    print 'Got connection from', addr
    data = conn.recv(1024)
    if data:
        print('Server received', repr(data))
        print "Insert file to send"
        filename = raw_input()
        encrypted_data = cypher.encrypt_file(filename)
        conn.send(encrypted_data)
        print 'Done sending'
        conn.close()
    flag = False

#Jellyfish.jpg