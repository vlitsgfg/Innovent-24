<?php
 include('connection.php');
 if (isset($_POST['submit'])) {
    $username = $_POST['user'];}
 ?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-compatible" content="IE-edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home page</title>
    <link rel="stylesheet" type="text/css" href="home.css">
</head>
<body>
    <img id="img" src="https://vignanslara.live/exam/images/logo/lara.png">
    <h2>Welcome user!!</h2>
    <form action="feestructure.php"><input type="submit" id="btn" name="submit" value="Fee Structure"></form></br></br>
    <form action="checkfee.php"><input type="submit" id="btn" name="submit" value="Check Fee"></form></br></br>
    <form action="logout.php"><input type="submit" id="btn" name="submit" value="Logout"></form>
</body>
</html>
