#!C:\laragon\www\dict\Env\Scripts\python.exe
import sys
from sys import argv
from struct import *
import io
print("Content-type: text/html\n\n")

def decompressText(data):
    # Membuka dan menginisialisasi dictionary
    file = open(data, "rb")
    compressed_data = []
    next_code = 256
    decompressed_data = ""
    string = ""

    # Membaca file LZW
    while True:
        rec = file.read(2)
        if len(rec) != 2:
            break
        (data, ) = unpack('>H', rec)
        compressed_data.append(data)

    # Membangun dan inisialisasi Dictionary
    dictionary_size = 256
    dictionary = dict([(x, chr(x)) for x in range(dictionary_size)])

    # Iterasi untuk algoritma LZW Decompression
    for code in compressed_data:
        if not (code in dictionary):
            dictionary[code] = string + (string[0])
        decompressed_data += dictionary[code]
        if not(len(string) == 0):
            dictionary[next_code] = string + (dictionary[code][0])
            next_code += 1
        string = dictionary[code]

    # Menyimpan string hasil decompression dalam file
    output_file = open("files/decompressed.txt", "w")
    for data in decompressed_data:
        output_file.write(data)
    
    return output_file
    #file.close()

filename = "files/compressed_lzw.lzw"

encrypted_filename = decompressText(filename)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>APA INI</title>
    <!-- Compiled and minified CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
    <link rel="stylesheet" href="#">
</head>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dictionary Decompression</title>

    <!-- Compiled and minified CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">

    <link rel="stylesheet" href="#">
</head>
<nav>
        <div class="nav-wrapper">
            <div class="container">
                <a href="index.html" class="brand-logo">Decompression</a>
            </div>
        </div>
    </nav>
<body>
<br>
    <div class="container">
        <div class="row">
            <h4>Decompressed Text</h4>
        </div>
        <div class="row">
            <div class="col">Output: </div>
        </div>
        <div class="row">
            <div class="col s6">
                <a class="button" href="files/decompressed.txt">Output</a>
            </div>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
</body>
</html>
"""
print(html)