<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>fee details</title>
    <style>
        *{
            font-family: Arial, Helvetica, sans-serif;
            margin: 0px;
        }
        body{
            background-image: linear-gradient(to bottom right, rgb(113, 204, 222), blueviolet);
            height: 100vh;
        }
        main h2, main h3{
            margin:5px;
            padding:5px;
        }
        main h2{
            border: 1px solid blueviolet;
            border-radius:5px ;
        }
        header{
            text-align: center;
            padding: 20px;
            top: 0px;
            margin: auto;
            border-bottom: 1px solid blueviolet;
            background-color: white;
            margin-bottom: 100px;
        }
        main{
            margin-top: 100px;
            width: 900px;
            margin-left: auto;
            margin-right: auto;
            background-color: white;
            padding: 25px;
        }
        footer{
            background-color: #666;
            color: white;
            bottom: 0px;
            width: 100%;
            position: absolute;
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            padding: 10px;
        }
    </style>
</head>
<body>
    <header>
        <h1>VIGNAN'S LARA INSTITUE OF TECHNOLOGY AND SCIENCE</h1>
    </header>
    <?php
                session_start();
                $db=mysqli_connect("localhost","root","","fee");
                $a = $_SESSION['username'];
                $que="SELECT * FROM daily_fees where Regno='$a'";
                $q=mysqli_query($db,$que);
                $r=mysqli_num_rows($q);
                while($r = mysqli_fetch_array($q)){
                    $_SESSION['Name']=$r['Name'];
                    $_SESSION['Regno']=$r['Regno'];
                    $_SESSION['Branch']=$r['Branch'];
                    //$_SESSION['Name']=$r['Regno'];
                }                   
?>
    <main>

        <div>
             <h3>Name: </h3><?php echo $_SESSION['Name']  ?>

            <h3 >Regd no: </h3> <?php echo $_SESSION['Regno'] ?>

            <h3 >Branch: </h3> <?php echo $_SESSION['Branch']  ?>
        </div>
    </main>
</body>
</html>