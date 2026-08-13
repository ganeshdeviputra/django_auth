document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.site-nav');
  const links = document.querySelectorAll('.nav-links a');

  if (!toggle || !nav) return;

  toggle.addEventListener('click', () => {
    nav.classList.toggle('is-open');
  });

  links.forEach((link) => {
    link.addEventListener('click', () => {
      nav.classList.remove('is-open');
    });
  });

  window.addEventListener('resize', () => {
    if (window.innerWidth > 860) {
      nav.classList.remove('is-open');
    }
  });
});
