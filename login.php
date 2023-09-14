<?php
// Check if form is submitted
if(isset($_POST['submit'])) {

    // Establish database connection
    $servername = "localhost";  // Replace with your database server name
    $username = "root";         // Replace with your database username
    $password = "";             // Replace with your database password
    $dbname = "tour";           // Replace with your database name
    $conn = mysqli_connect($servername, $username, $password, $dbname);

    // Check database connection
    if (!$conn) {
        die("Connection failed: " . mysqli_connect_error());
    }
    else{
        echo "logged in successfully";
    }

    // Get login details from form
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Insert login details into database
    $sql = "INSERT INTO login (username, password) 
            VALUES ('$username', '$password')";

    if (mysqli_query($conn, $sql)) {
       // echo "New record created successfully";
       header("Location: home.html");
       exit();
    } else {
        echo "Error: " . $sql . "<br>" . mysqli_error($conn);
    }

    // Close database connection
    mysqli_close($conn);
}
?>