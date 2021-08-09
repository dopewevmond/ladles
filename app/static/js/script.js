const year_element = document.getElementsByClassName('js-current-year')[0];
const current_year = new Date().getFullYear();
// console.log(current_year);
document.addEventListener('DOMContentLoaded', () => {
    year_element.innerHTML = current_year;
});