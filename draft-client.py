"""
Client that sends the file (uploads)
"""
import socket #import library
import tqdm
import os
import argparse

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 1024 * 4 #4KB
HOST = '127.0.0.1'  
PORT = 4444   

def recieveFile(s):
    # Menerima info dari file
    # Menerima file dari server dengan s.recv
    received = s.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)
    # Menghilangkan path jika ada
    filename = os.path.basename(filename)
    # mengubah ke int besar filenya
    filesize = int(filesize)
    # Mulai untuk menerima file
    progress = tqdm.tqdm(range(filesize), f"\nReceiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    #dg bantuan library tqdm dengan format bit
    with open(filename, "wb") as f: #dibuka file namenya
        while True:
            # Membaca data file dari server
            bytes_read = s.recv(BUFFER_SIZE)
            if not bytes_read:    
                break
            # Memasukkan ke file
            f.write(bytes_read)
            #Mengupdate progress bar
            progress.update(len(bytes_read))

if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #af inet utk ip adres
        #v4 dan sock stream untuk tcp
        s.connect((HOST, PORT))    #connect port dan host     
        print("===========================================================================")
        print("Masukkan Nama File: ")
        filename2 = input()
        fileku = open(filename2, "rb") 
        data = fileku.read()
        fileku.close()
        s.send(data) #untuk mengiitim ke server dg s.send (filenya ms lom dikomres)
        server = s.recv(1024).decode('utf-8') #menerima info ttg nama dan ukuran file dlm byte
        print(server)
        print("\nSilahkan Memilih Opsi Berikut:\ncompress text : c\ndecomppress text : d\nquit : q")
        option = input()
        s.send(bytes(option,'utf-8'))
        if option == 'c':
            recieveFile(s) #untuk menemrima file hasil kompres dan dikompres dari send_file()
        elif option == 'd':
            recieveFile(s)
        
        s.close()
