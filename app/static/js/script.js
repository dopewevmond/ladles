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

const accessToken = 'pk.eyJ1IjoiZG9wZXdldm1vbmQiLCJhIjoiY2txdmxrbnowMGZyeTJwbzZlNmd6cXlzciJ9.iI1yRNIsCr9lvfjeoXVteg';
var mapboxTiles = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/{z}/{x}/{y}?access_token=' + accessToken, {
       attribution: '© <a href="https://www.mapbox.com/feedback/">Mapbox</a> © <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
       tileSize: 512,
       zoomOffset: -1
});

const lat = 5.6374
const lng = -0.1848
var map = L.map('map')
  .addLayer(mapboxTiles)
  .setView([lat, lng], 15);
  var marker = L.marker([lat, lng]).addTo(map);
