
document.getElementById('goToSpecialsPageButton').addEventListener('click', function() {
  window.location.href = '/specials'; // Относительный путь к другой странице
});

const swiper = new Swiper(".swiper", {
    effect: "fade",
    pagination: {
      el: ".swiper-pagination",
      dynamicBullets: true,
    },
    autoplay: {
      delay: 3000,
      disableOnInteraction: false,
    },
});



