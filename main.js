document.addEventListener('DOMContentLoaded', () => {
  const indicator = document.getElementById('status-indicator');
  console.log('Core UI Framework successfully initiated.');
  setInterval(() => {
    indicator.style.opacity = indicator.style.opacity === '0' ? '1' : '0';
  }, 1000);
});