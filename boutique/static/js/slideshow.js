document.addEventListener('DOMContentLoaded', function() {
  const slideshow = document.querySelector('.slideshow');
  if (!slideshow) {
    return;
  }

  const slides = slideshow.querySelectorAll('.slide');
  if (slides.length <= 1) {
    return;
  }

  let currentSlideIndex = -1;
  for (let i = 0; i < slides.length; i++) {
    if (slides[i].classList.contains('active')) {
      currentSlideIndex = i;
      break;
    }
  }

  if (currentSlideIndex === -1 && slides.length > 0) {
    currentSlideIndex = 0;
    slides[0].classList.add('active');
    for (let i = 1; i < slides.length; i++) {
        slides[i].classList.remove('active');
    }
  } else if (currentSlideIndex === -1 && slides.length === 0) {
    return;
  }

  const slideInterval = 5000; // 5 seconds

  setInterval(() => {
    if (slides[currentSlideIndex]) {
        slides[currentSlideIndex].classList.remove('active');
    }
    currentSlideIndex = (currentSlideIndex + 1) % slides.length;
    if (slides[currentSlideIndex]) {
        slides[currentSlideIndex].classList.add('active');
    }
  }, slideInterval);
});