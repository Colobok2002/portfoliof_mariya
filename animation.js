function onEntry(entry) {
    entry.forEach(change => {
      if (change.isIntersecting) {
       change.target.classList.add('element-show');
      } else {
        change.target.classList.remove('element-show');
      }
    });
  }
  
//let options = {threshold: [0.00, 0.01, 0.02, /*…,*/ 0.99, 1.00]};
let options = {threshold: [0.4]};
let observer = new IntersectionObserver(onEntry, options);
let elements = document.querySelectorAll('section , .header__text , .about__content, .header__text-box.row , .my_work');
console.log(elements);
  
for (let elm of elements) {
    observer.observe(elm);
  }