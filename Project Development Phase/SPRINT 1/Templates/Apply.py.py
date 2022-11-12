<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JOBPORTAL | APPLY</title>
        <!-- favicon -->
        <!-- <link rel="shortcut icon" href="/assets/img/favicon.ico" type="image/x-icon"> -->
        <!-- <link rel="icon" href="/assets/img/favicon.ico" type="image/x-icon"> -->
        <link rel="icon" type="image/jpg
        " sizes="16x16" href="/assets/img/favicon-32x32.png">
        <!-- bootstrap css cdn -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css">
        <!-- css stylesheet -->
        <link rel="stylesheet" href="css/style.css">
        <!-- font styles cdn -->
        <link rel="preconnect" href="https://fonts.gstatic.com">
        <link href="https://fonts.googleapis.com/css2?family=Alegreya&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Alegreya:wght@600&display=swap" rel="stylesheet">
</head>
<body>
    <!-- bootstrap navbar -->
    <div class="logo mt-3 text-center">
        <a class="main-logo-img mt-5" href=".png"><img src="" alt="" height="50px" width="180px">
            <!-- <a class="navbar-brand" href="index.html">JobPortal</a> -->
          </a>
    </div>
      <!-- navbar ends -->
    <!-- Login form -->
    <div class="login text-center mt-5"> 
        <h2>Apply Now</h2>
        <div class="msg">{{ msg }}</div>
        <form action="/apply" method="post" class="mt-3">
            <!-- <input type="text" placeholder="fullname" id="fullname"> </br></br> -->
            <input type="text" name="username" placeholder="Enter Your Username"  id="username" required></br></br>
            <input type="email" name="email" placeholder="Enter Your email"  id="email" required></br></br>
            <input type="text" name="qualification" placeholder="Enter Your Qualification"  id="qualification" required></br></br>
			<input type="text" name="skills" placeholder="Enter Your skills" id="skills" required></br></br>
            
         
              <select name ="s">
<option value ="PYTHON"> Python</option>
<option value ="ML"> ML</option>
<option value ="AI"> AI</option>
</select>
            </br></br>
        <button type="submit" id="button" class="btn btn-primary"> Submit</button>
        </form>
    </div>

 <div class="note mt-3 text-center">
    <p> click here to go to dashboard <a href="dashboard">Dashboard! </a> </p>
   
    
    </div>
</body>
</html>