<!DOCTYPE html>
<html style="font-size: 16px;" lang="en"><head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="utf-8">
    <meta name="keywords" content="">
    <meta name="description" content="">
    <title>student login</title>
    <link rel="stylesheet" href="nicepage.css" media="screen">
<link rel="stylesheet" href="student-login.css" media="screen">
    <script class="u-script" type="text/javascript" src="jquery.js" defer=""></script>
    <script class="u-script" type="text/javascript" src="nicepage.js" defer=""></script>
    <meta name="generator" content="Nicepage 5.17.1, nicepage.com">
    <meta name="referrer" content="origin">
    <link id="u-theme-google-font" rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i|Open+Sans:300,300i,400,400i,500,500i,600,600i,700,700i,800,800i">
    <link id="u-page-google-font" rel="stylesheet" href="https://fonts.googleapis.com/css?family=Merriweather:300,300i,400,400i,700,700i,900,900i">
    
    
    
    <script type="application/ld+json">{
		"@context": "http://schema.org",
		"@type": "Organization",
		"name": ""
}</script>
    <meta name="theme-color" content="#478ac9">
    <meta property="og:title" content="student login">
    <meta property="og:type" content="website">
  <meta data-intl-tel-input-cdn-path="intlTelInput/"></head>
  <body class="u-body u-xl-mode" data-lang="en">
    <section class="u-clearfix u-section-1" id="carousel_9522">
      <div class="u-clearfix u-sheet u-sheet-1">
        <div class="u-align-left u-image u-image-circle u-image-1" data-image-width="1280" data-image-height="853"></div>
        <div class="u-expanded-width-xs u-form u-palette-1-light-3 u-radius-10 u-form-1">
          <form method = "post"   style="padding: 28px;">
            <div class="u-form-group u-form-name">
              <label for="name-4c18" class="u-custom-font u-font-merriweather u-label u-label-1">Name</label>
              <input type="text" placeholder="Enter your Name" id="name-4c18" name="name" class="u-border-2 u-border-grey-90 u-custom-font u-font-merriweather u-input u-input-rectangle u-palette-1-base u-radius-15 u-input-1" required="">
            </div>
            <div class="u-form-email u-form-group">
              <label for="email-4c18" class="u-custom-font u-font-merriweather u-label u-label-2">password</label>
              <input type="password" placeholder="enter password" id="email-4c18" name="password" class="u-border-2 u-border-grey-90 u-custom-font u-font-merriweather u-input u-input-rectangle u-palette-1-base u-radius-15 u-input-2" required="" style="u-active-palette-1-light-1 u-border-2 u-border-active-palette-1-light-1 u-border-hover-palette-1-light-1 u-border-palette-1-base u-btn u-btn-round u-btn-submit u-button-style u-hidden-lg u-hover-palette-1-light-1 u-palette-1-base u-radius-10 u-btn-1" bgcolor="#800080">
            </div>
          <!--  <div class="u-align-center u-form-group u-form-submit">
              <a href="#" class="u-active-palette-1-light-1 u-border-2 u-border-active-palette-1-light-1 u-border-hover-palette-1-light-1 u-border-palette-1-base u-btn u-btn-round u-btn-submit u-button-style u-hidden-lg u-hover-palette-1-light-1 u-palette-1-base u-radius-10 u-btn-1"></a>
               </div>-->
               <center><br>
          <input type="submit" value="submit" name = "submit" ></center>
         
          </form>
       
		<!--<h2 class="u-btn u-btn-round u-button-style u-hover-palette-1-light-1 u-palette-1-base u-radius-6 u-btn-2">submit</h2>
      </div>-->
    </section>
    
    
    
</body></html>
<?php
session_start();
//echo "Hello world";
$db =mysqli_connect("localhost","root","","fee");
if(isset($_POST['submit'])){
$name = $_POST['name'];
$pass  = $_POST['password']; 
$query="SELECT * FROM stu_login where isername='$name' and password='$pass'";
$result=mysqli_query($db,$query);
$row=mysqli_num_rows($result);
if($row > 0){
$_SESSION['username']=$name;
echo "successfully logined";
//header("location:index.php");
?>
<script>

window.location.assign("student-submit.html");


</script>
<?php
}
 else {
  echo "<h7><span style = color: red>bab credentials";
}
}

?>