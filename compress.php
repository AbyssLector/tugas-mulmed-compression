<?php
if (isset($_POST['submit'])) {
    $info = pathinfo($_FILES['plain_file']['name']);
    $ext = $info['extension']; // get the extension of the file
    // $newname = "plain_file." . $ext;
    $newname = "plain_file." . "txt";

    move_uploaded_file($_FILES['plain_file']['tmp_name'], $newname);
    header("location: compress.py");
}

?>
<!-- Buat page awal -->
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
            <form class="col s12" action="#" method="post" enctype="multipart/form-data">
                <div class="row">
                    <div class="col s6">
                        <input type="file" name="plain_file" id="plain_file">
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
    <button>

    </button>

    <!-- Compiled and minified JavaScript -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
</body>

</html>