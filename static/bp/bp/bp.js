document.getElementById("date").innerHTML=(Date());

function mOver1(obj){
    obj.innerHTML="首页"
}
function mOut1(obj){
    obj.innerHTML="Home"
}

function mOver2(obj){
    obj.innerHTML="简况"
}
function mOut2(obj){
    obj.innerHTML="Profile"
}

function mOver3(obj){
    obj.innerHTML="作品"
}
function mOut3(obj){
    obj.innerHTML="Works"
}

function mOver4(obj){
    obj.innerHTML="注册"
}
function mOut4(obj){
    obj.innerHTML="Sign Up"
}


var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1} 
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none"; 
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block"; 
  dots[slideIndex-1].className += " active";
}

function openModal() {
    document.getElementById('myModal').style.display = "block";
  }
   
  function closeModal() {
    document.getElementById('myModal').style.display = "none";
  }
   
  var slideIndex = 1;
  showSlides(slideIndex);
   
  function plusSlides(n) {
    showSlides(slideIndex += n);
  }
   
  function currentSlide(n) {
    showSlides(slideIndex = n);
  }
   
  function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    var dots = document.getElementsByClassName("demo");
    var captionText = document.getElementById("caption");
    if (n > slides.length) {slideIndex = 1}
    if (n < 1) {slideIndex = slides.length}
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex-1].style.display = "block";
    dots[slideIndex-1].className += " active";
    captionText.innerHTML = dots[slideIndex-1].alt;
  }