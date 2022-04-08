<?php
if (isset($_POST['submit'])) {
    $info = pathinfo($_FILES['plain_text']['name']);
    $ext = $info['extension']; // get the extension of the file
    $newname = "plain_text." . $ext;

    // $target = 'images/' . $newname;
    move_uploaded_file($_FILES['plain_text']['tmp_name'], "files/".$newname);
    header("location: fileCompress.py");
}
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>APAPULA</title>

    <!-- Compiled and minified CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">

    <link rel="stylesheet" href="#">
</head>
<body>
<div class="container">
    <div class="row">
        <form class="col s12" action="#" method="post" enctype="multipart/form-data">
            <div class="row">
                <div class="col s6">
                    <!-- <input type="file" name="plain_img"> -->
                    <input type="file" name="plain_text" id="plain_text">
                    <img id="output" width="200" />
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
