 let currentIndex = 0;
  const images = document.querySelectorAll('.carousel-item');
  const totalImages = images.length;

  function showNextImage() {
    images[currentIndex].style.display = 'none';
    currentIndex = (currentIndex + 1) % totalImages; 
    images[currentIndex].style.display = 'block'; 
  }


  images[currentIndex].style.display = 'block';


  setInterval(showNextImage, 4000);