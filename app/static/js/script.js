const year_element = document.getElementsByClassName('js-current-year')[0];
const current_year = new Date().getFullYear();
// console.log(current_year);
document.addEventListener('DOMContentLoaded', () => {
    year_element.innerHTML = current_year;

    var currencies = document.getElementsByClassName('js-decimal');
    for (let i=0; i<currencies.length; i++) {
        currencies[i].innerHTML = parseFloat(currencies[i].innerHTML).toFixed(2);
    }
});

// Initialize and add the map
function initMap() {
    // The location of Uluru
    const uluru = { lat: 5.63749, lng: -0.18488};
    // The map, centered at Uluru
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 4,
      center: uluru,
    });
    // The marker, positioned at Uluru
    const marker = new google.maps.Marker({
      position: uluru,
      map: map,
    });
  }