import socket
import numpy as np


if __name__ == '__main__':
    original = str(input("masukkan kata2 : "))
    key = int(input("masukka angka untuk enkripsi : "))

    kunci = np.asarray([ord(kunci) for kunci in original])
    terkunci = kunci + key
    enkripsi = ''.join(map(chr, terkunci))
    print("encrypted : %s" % enkripsi)

    host = socket.gethostname()
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((host, port))

    s.sendall(b'%s' % enkripsi)
    #s.send(b'%i' % key)
    enkripsi = s.recv(2048)
    #key = s.recv(1024)
    s.close()
    print('Received', repr(enkripsi))
