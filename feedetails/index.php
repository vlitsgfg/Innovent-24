<?php
   include("connection.php");
   include("login.php");
?>   
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-compatible" content="IE-edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="index.css">
    <title>Fee Details</title>
</head>
<body>
   <div id="form">
      <img id="img" src="https://www.vignanlara.org/images/logo/lara.png"/>
      <h1 id="heading">Login form</h1>
      <form name="form" action="login.php" onsubmit="return isvalid()" method="POST">
        <label id="heading">Student Id :</label>
        <input type="text" id="user" name="user"></br></br>
        <label id="heading" >Password :</label>
        <input type="password" id="pass" name="pass"></br></br>
        <input type="submit" id="btn" value="Login" name="submit"> 
      </form>
   </div>    
   <script>
    function isvalid(){
       var user = doucument.form.user.value;
       var pass = document.form.pass.value;
       if(user.length=="" && pass.length==""){
       alert("Please Student Id and Password!");
       return false;
       }
       else if(user.length==""){
        alert("Please enter StudentId!!");
        return false;
       }
       else if(pass.length==""){
        alert("Please enter Password!!");
        return false;
       }
    }
    </script>
</body>
</html>