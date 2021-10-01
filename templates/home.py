<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Ubuntu:wght@700&display=swap" rel="stylesheet">
    <title>Home</title>
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
    <center>
        <h1><u><em>WELCOME TO THIS WORD COUNT WEBSITE!!</em></u></h1>
    </center>
    <p>The Word Count Is The Number Of Words In A Document Or In A Passage Of Text. Word Counting May Be Needed When A Text Is Required To Stay Within Certain Numbers Of Words.Word Counts May Also Be Used To Calculate Measures Of Readability And To Measure Typing And Reading Speeds.In This Application,We Also Present The Dictionary Order of the words is also displayed. </p>
    <img src="https://awario.com/upload/blog/trump-all-final.png?1547133106384" alt="word" width="750" height="330">
    <img src="https://awario.com/upload/blog/trump-3.png?1547133212256" alt="word" width="730" height="330">
</body>
</html>
