#!C:\laragon\www\dict\Env\Scripts\python.exe
import sys
from sys import argv
from struct import *
print("Content-type: text/html\n\n")

def compressText(data):
    # Membangun dan menginisialisasi dictionary
    file = open(data)                 
    data = file.read()                      

    dictionary_size = 256                   
    dictionary = {chr(i): i for i in range(dictionary_size)}    
    string = ""             # String adalah NULL
    compressed_data = []    # Variabel untuk menyimpan data hasil compression

    # Iterasi karakter yang ada
    # Dilanjutkan Algoritma kompresi LZW
    for symbol in data:                     
        string_plus_symbol = string + symbol # Mendapatkan simbol
        if string_plus_symbol in dictionary: 
            string = string_plus_symbol
        else:
            compressed_data.append(dictionary[string])
            dictionary[string_plus_symbol] = dictionary_size
            dictionary_size += 1
            string = symbol

    if string in dictionary:
        compressed_data.append(dictionary[string])

    # Menyimpan compressed string ke dalam file 
    output_file = open("files/compressed.lzw", "wb") 
    #membuka file untuk menyimpan hasil compress
    for data in compressed_data:
        output_file.write(pack('>H',int(data))) 
        #memasukan file dalam bentuk binary deg bantuan struck.pack
        #>h yang menandakan big endian unsigned sort
        
    return output_file
    #output_file.close()
    #file.close()

filename = "files/plain_text.txt"

encrypted_filename = compressText(filename)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dictionary Compression</title>
    <!-- Compiled and minified CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
    <link rel="stylesheet" href="#">
</head>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dictionary Compression</title>

    <!-- Compiled and minified CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">

    <link rel="stylesheet" href="#">
</head>
<nav>
        <div class="nav-wrapper">
            <div class="container">
                <a href="index.html" class="brand-logo">Compression</a>
            </div>
        </div>
    </nav>
<body>
<br>
    <div class="container">
        <div class="row">
            <h4>Compressed Text</h4>
        </div>
        <div class="row">
            <div class="col">Output: </div>
        </div>
        <div class="row">
            <div class="col s6">
                <div class="card-panel">
                    <a href="files/compressed.lzw">Output</a>
                </div>
            </div>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
</body>
</html>
"""
print(html)