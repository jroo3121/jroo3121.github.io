
<head>
  <link rel="shortcut icon" type="image/x-icon" href="favicon.ico" />
      <style>
              .loader,
        .loader:after {
            border-radius: 50%;
            width: 10em;
            height: 10em;
        }
        .loader {            
            margin: 60px auto;
            font-size: 10px;
            position: relative;
            text-indent: -9999em;
            border-top: 1.1em solid #000000;
            border-right: 1.1em solid #FFFFFF;
            border-bottom: 1.1em solid #000000;
            border-left: 1.1em solid #000000;
            -webkit-transform: translateZ(0);
            -ms-transform: translateZ(0);
            transform: translateZ(0);
            -webkit-animation: load8 1.1s infinite linear;
            animation: load8 1.1s infinite linear;
        }
        @-webkit-keyframes load8 {
            0% {
                -webkit-transform: rotate(0deg);
                transform: rotate(0deg);
            }
            50% {
                -webkit-transform: rotate(220deg);
                transform: rotate(220deg);
            }
            100% {
                -webkit-transform: rotate(360deg);
                transform: rotate(360deg);
            }
        }
        @keyframes load8 {
            0% {
                -webkit-transform: rotate(0deg);
                transform: rotate(0deg);
            }
            50% {
                -webkit-transform: rotate(220deg);
                transform: rotate(220deg);
            }
            100% {
                -webkit-transform: rotate(360deg);
                transform: rotate(360deg);
            }
        }
        #loadingDiv {
            position:absolute;;
            top:0;
            left:0;
            width:100%;
            height:100%;
            background-color:#000;
        }
        .texty {
          color: white;
        }


    </style>
</head>
  <body>
  <center><h1>Hey everyone!</h1></center>
  Hey guys! My name is Jonah, but most people call me jroo3121. I've always loved coding. I can code in multiple languages, such as, 
  <ul>
  <li>Java</li>
  <li>JS</li>
  <li>C#</li>
  <li>Scratch</li>
</ul>
  
    <p>And HTML and CSS for web developpement. </p>
    <p>
    
    <h1><a href="https://jroo3121.github.io/games.html">Games</a></h1>  
    <p>
    <h1><a href="https://jroo3121.github.io/discordbots.html">Discord Bots</a></h1>
    <p>
    <h1><a href="https://jroo3121.github.io/randomstuff.html">Miscellaneous Projects</a></h1>  
    <p>
    <h4>Contact me on Discord! jroo3121#7367</h4>
    <h3><a href="https://discord.gg/xa5WGCPmtz">Join the Discord Server!</a></h3>
    <p>
    <h5><a href="https://jroo3121.github.io/friends.html">Friends' Websites</a></h5>
    
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
<script>
      
$('body').append('<div style="" id="loadingDiv"><div class="loader texty">Loading...</div></div>');
$(window).on('load', function(){
  setTimeout(removeLoader, 1000); //wait for page load PLUS two seconds.
});
function removeLoader(){
    $( "#loadingDiv" ).fadeOut(600, function() {
      // fadeOut complete. Remove the loading div
      $( "#loadingDiv" ).remove(); //makes page more lightweight 
  });  
}
</script>
 </body>
 
      
      

