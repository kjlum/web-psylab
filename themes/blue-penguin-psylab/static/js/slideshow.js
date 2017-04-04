window.onload = function(e) {
  var slideIndex = 0;
  showSlides(slideIndex);

  function plusSlides(n) {
    showSlides(slideIndex += n);
  }

  function currentSlide(n) {
    showSlides(slideIndex = n);
  }

  var dots = document.getElementsByClassName("dot");
  for(var i = 0; i < dots.length; i++) {
    dots[i].onclick = (function() {
      var currentI = i;
      return function() {
        currentSlide(currentI);
      }
    })();
  }

  var next = document.getElementById("next");
  next.onclick = (function() {
    return function() {
      plusSlides(1);
    }
  })();

  var prev = document.getElementById("prev");
  prev.onclick = (function() {
    return function() {
      plusSlides(-1);
    }
  })();

  function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    var dots = document.getElementsByClassName("dot");
    if (n == slides.length) {
      slideIndex = 0;
    } 
    if (n < 0) {
      slideIndex = slides.length - 1;
    }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none"; 
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex].style.display = "block"; 
    dots[slideIndex].className += " active";
  }

  function showSlidesAuto() {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none"; 
    }
    currentSlide(slideIndex);
    slideIndex++;
    if (slideIndex == slides.length) {
      slideIndex = 0;
    }
    setTimeout(showSlidesAuto, 5000); // Change image every 5 seconds
  }

  showSlidesAuto();
};