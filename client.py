import socket
from present_implementation import PresentCypherImplementation
s = socket.socket()
print "Insert server ip"
host = raw_input()
print "Insert port"
port = int(raw_input())
encrypted_data = ""

s.connect((host, port))
s.send("Hello server!")
cypher = PresentCypherImplementation()

while True:
    data = s.recv(8192)
    print "Receiving Data"
    encrypted_data += data
    if not data:
        break
if encrypted_data:
    cypher.decrypt_file(encrypted_data)
    print 'Successfully get the file'
else:
    print "SOMETHING WENT WRONG"

s.close()
print 'connection closed'