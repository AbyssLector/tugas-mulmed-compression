"""
Client that sends the file (uploads)
"""
import socket
import tqdm
import os
import sys
from sys import argv
from struct import *
import io

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 1024 * 4 #4KB
HOST = '127.0.0.1'
PORT = 4444

def compressText(data):

    # buat dictionary
    dictionary_size = 256      #inisialisasi 256 char sheet             
    dictionary = {chr(i): i for i in range(dictionary_size)}  
    string = ""             # string awalnya null. tempat menyimpan input character(substring)
    compressed_data = []    # variable menyimpan compressed data.

    # iterasi input character (c)
    # LZW Compression algorithm
    for c in data:                     
        string_plus_char = string + c 
        if string_plus_char in dictionary: # jika string + char ada di tabel maka tidak perlu output dulu
            string = string_plus_char
        else:
            compressed_data.append(dictionary[string]) # jika belum ada dimasukkan ke output.
            dictionary[string_plus_char] = dictionary_size # tambahkan ke table.
            dictionary_size += 1 #dictionary size di increment
            string = c #mereset nilai variable string dengan c

    if string in dictionary: 
        compressed_data.append(dictionary[string]) # output untuk char terakhir.

    # menyimpan compressed string dalam file
    #mode wb yang berarti file dlm binary utk writing
    output_file = open("compressed.lzw", "wb") #menyimpan file utk dikirim ke client
    for data in compressed_data:
        output_file.write(pack('>H',int(data))) #memasukan file dalam bentuk binary deg bantuan struck.pack
        #>h yang menandakan big endian unsigned sort
    output_file.close()
  
def decompressText(data2):
    # membuka file compressed
    # define variabel2
    file = io.BytesIO(data2) 
    compressed_data = [] #menyimoan hasil kompres data sebelumnya
    next_code = 256 #index untuk kombinasi substring. 
    decompressed_data = "" #untuk menyimpan hasil dekompres
    string = "" #untuk menyimpan kombinasi substring

    # read compressed file
    while True: #while loop dg bantuan library unpack utk membuak file binary
        rec = file.read(2)
        if len(rec) != 2:
            break
        (data, ) = unpack('>H', rec)
        compressed_data.append(data)

    # membuat dictionary
    dictionary_size = 256 #mengisi dictionary dengan standart caharacter set
    dictionary = dict([(x, chr(x)) for x in range(dictionary_size)])

    # iterasi 
    # LZW Compression algorithm
    for code in compressed_data:
        decompressed_data += dictionary[code] # append satu persatu ke dalam output
        if not(len(string) == 0): # tambah kombinasi ke dictionary setiap ada kombinasi substring baru
            dictionary[next_code] = string + (dictionary[code][0]) # append 
            next_code += 1
        string = dictionary[code] # simpan ke string

    # menyimpan decompressed string dalam file
    output_file = open("decompress.txt", "w")
    for data in decompressed_data:
        output_file.write(data)
        
    output_file.close()


def send_file(conn,filename):
    # mendapatkan filesizenya
    filesize = os.path.getsize(filename)

    # mengirim namma file dan size
    conn.send(f"{filename}{SEPARATOR}{filesize}".encode())

    # Memulai mengirim
    progress = tqdm.tqdm(range(filesize), f"\nSending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
        while True:
            # membaca file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                
                break
            # mengirim data file
            conn.sendall(bytes_read)
            # mengupdate progress bar
            progress.update(len(bytes_read))

if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
        #AF_INET untuk IP adress
        #V4 dan SOCK_STREAM untuk TCP
        s.bind((HOST, PORT)) #untk menetukan host dan port
        s.listen() #melisten
        conn, addr = s.accept() #accept sisi client
        print('Connected by', addr)
        with conn:
            print("===========================================================================")
            print("Menunggu Menerima data file...")
            data = conn.recv(4096) #mendapatkan request dr client
            conn.send(b'Pesan dari server : Data File Telah Diterima')
            print("Menunggu Jawaban Client...")         
            answer = conn.recv(1024).decode('utf-8')  
            if answer == 'c':
                print("Melakukan Compress...")
                compressText(data.decode('utf-8'))
                send_file(conn,"compressed.lzw")  #mengirimkan hasil compress
                  #mengetahui file size dulu baru ngirim informasi degan conn.send 
            elif answer == 'd':
                print("Melakukan Decompress...")
                decompressText(data)
                send_file(conn,"decompress.txt") #mengirimkan hasil dekompres
                  #file dikirim secara berkala data file ke clinet sesuai buffer size
            conn.close()