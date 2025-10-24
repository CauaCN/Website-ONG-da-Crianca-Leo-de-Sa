 let currentIndex = 0;
  const images = document.querySelectorAll('.carousel-item');
  const totalImages = images.length;

  function showNextImage() {
    images[currentIndex].style.display = 'none'; // Esconde a imagem atual
    currentIndex = (currentIndex + 1) % totalImages; // Avança para a próxima imagem
    images[currentIndex].style.display = 'block'; // Exibe a próxima imagem
  }

  // Exibe a primeira imagem
  images[currentIndex].style.display = 'block';

  // Muda a imagem a cada 3 segundos
  setInterval(showNextImage, 4000);