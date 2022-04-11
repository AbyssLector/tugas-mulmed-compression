<?php
if (isset($_POST['submit'])) {
    $info = pathinfo($_FILES['compressed_lzw']['name']);
    $ext = $info['extension']; // get the extension of the file
    $newname = "compressed_lzw." . $ext;

    // $target = 'images/' . $newname;
    move_uploaded_file($_FILES['compressed_lzw']['tmp_name'], "files/".$newname);
    header("location: fileDecompress.py");
}
?>
<!DOCTYPE html>
<html lang="en">

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
        <form class="col s12" action="#" method="post" enctype="multipart/form-data">
            <div class="row">
                <div class="col s6">
                    <!-- <input type="file" name="plain_img"> -->
                    <input type="file" name="compressed_lzw" id="compressed_lzw">
                    </div>
                </div>
                <div class="row">
                    <div class="col s6">
                        <input type="submit" name="submit" class="btn waves-effect waves-light red">
                    </div>
                </div>
        </form>
    </div>
</div>
</body>