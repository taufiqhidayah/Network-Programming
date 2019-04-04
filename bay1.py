import socket
import numpy as np


host = ''
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

print (host, port)
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)
while True:

    try:
        enkripsi = conn.recv(2048)
        #key = conn.recv(1024)

        if not enkripsi: break

        print ("Client Says: "+enkripsi)
        conn.sendall("Server     Says:hi")
        buka = np.array([ord(buka) for buka in enkripsi])
        terbuka = buka - key
        decrypted = ''.join(map(chr, terbuka))
        print("decrypted : %s" % decrypted)

    except socket.error:
        print ("Error Occured.")
        break

conn.close()
