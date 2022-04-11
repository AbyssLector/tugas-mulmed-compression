#!C:\xampp\htdocs\huffman\Env\Scripts\python.exe
from huffman import HuffmanCoding

print("Content-type: text/html\n\n")
path = "plain_file.txt"

h = HuffmanCoding(path)

output_path = h.compress()

decom_path = h.decompress(output_path)
html = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File | Compression</title>

    <!-- Compiled and minified CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">

</head>

<body>
    <nav>
        <div class="nav-wrapper">
            <div class="container">
                <a href="index.html" class="brand-logo">Compression</a>
            </div>
        </div>
    </nav>

    <div class="container">
        <div class="row">
            <h4>File Compression</h4>
        </div>
        <div class="row">
            <a href="{}" class="btn waves-effect waves-light red">Result</a>
            <a href="{}" class="btn waves-effect waves-light red">Decompressed Result</a>
        </div>
    </div>

    <!-- Compiled and minified JavaScript -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
</body>

</html>
""".format(output_path, decom_path)
print(html)

