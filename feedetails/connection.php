<?php
$servername="localhost";
$Student_Id="root";
$Password="";
$db_name="fee_details";
$conn= new mysqli($servername, $Student_Id, $Password, $db_name);
if($conn->connect_error){
    die("connection Failed".$conn->connect_error);
}
//echo " ";
?>