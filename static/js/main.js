// Auto-dismiss messages
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.alert').forEach(el => {
    setTimeout(() => el.remove(), 4000);
  });

  // Add active class to current nav category link
  const currentPath = window.location.pathname + window.location.search;
  document.querySelectorAll('.cat-inner a').forEach(link => {
    if (link.getAttribute('href') === currentPath) {
      link.classList.add('active');
    }
  });

  // Smooth add-to-cart feedback
  document.querySelectorAll('.add-cart-form, form[action*="add_to_cart"]').forEach(form => {
    form.addEventListener('submit', function() {
      const btn = form.querySelector('button[type="submit"]');
      if (btn) {
        btn.innerHTML = '<i class="fas fa-check"></i> Added!';
        btn.style.background = 'var(--success)';
      }
    });
  });
});
