// Función para manejar el comportamiento del acordeón
function toggleAccordion(index) {
  var items = document.getElementsByClassName('accordion-item');
  var content = items[index].querySelector('.content');
  
  for (var i = 0; i < items.length; i++) {
      var item = items[i];
      var itemContent = item.querySelector('.content');
      
      if (i === index) {
          item.classList.toggle('active');
          itemContent.style.display = itemContent.style.display === 'block' ? 'none' : 'block';
      } else {
          item.classList.remove('active');
          itemContent.style.display = 'none';
      }
  }
}
