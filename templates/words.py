<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Ubuntu:wght@700&display=swap" rel="stylesheet">
    <title>Word Counter</title>
</head>
<style>
     body{
    font-family: 'Ubuntu', sans-serif;
    color: black;
  }
  .navbar {
    overflow: hidden;
    text-align: center;
   
  }
  .navbar a {
    float: left;
    font-size: 16px;
    color:black;
    text-align: center;
    padding:22px;
    text-decoration: none;
    margin-top: 4px;
  }
  
  * {
    box-sizing: border-box;
  }
  .column {
    float: left;
    margin-left: 5px;
    width: 330px;
    padding: 5px;
  }
  .row::after {
    content: "";
    clear: both;
    display: table;
  }
  a{
      text-decoration: none;
      color:white;
  }
  
  #design{
    background-color:black;
    border: none;
    color: white;
    padding: 8px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 12px;
    font-family: 'Ubuntu', sans-serif;
  }
  .formelement{
    border: 5px solid black;
    padding-top: 10px;
    padding-bottom: 10px;
    background-image: linear-gradient(#54e346,black);
    font-family: 'Ubuntu', sans-serif;
  }
  
</style>
<body>

    <div class="navbar">
        <a href="{% url 'home' %}"><img src="https://svgsilh.com/svg_v2/146017.svg" alt="" srcset="" width="70" height="20"></a>
        <a href="{% url 'about' %}">ABOUT</a>
        <a href="{% url 'words' %}">WORD COUNTER</a>
        <br><br>
    </div>
    <h2><u>Enter The Text In The Area Provided</u></h2>
    <form action="{% url 'count' %}">
        <textarea name="fulltext" cols="80" rows="10" required></textarea><br><br>
        <input type="submit" value="COUNT" id="design">
    </form>    
</body>
</html>
