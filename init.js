//Hello
//this is a comment
 var gateways = {
  tub: {
    center: {lat: 52.5125322, lng: 13.3247559},
    radius: 150
  },
  fluxport: {
    center: {lat: 52.49782, lng: 13.3051813},
    radius: 250
  },
  kadewe: {
    center: {lat: 52.5016021, lng: 13.3388043},
    radius: 150
  },
  home: {
    center: {lat: 52.5414599, lng: 13.3502726},
    radius: 200
  },
  schloss: {
    center: {lat: 52.5209312, lng: 13.2781041},
    radius: 150
  }
};

function initMap() {
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 10,
    center: {lat: 52.5125322, lng: 13.3247559},
    //center: {lat: 52.5155893, lng: 13.2761299},
    mapTypeId: google.maps.MapTypeId.TERRAIN
  });

  for (var gateway in gateways) {
    var cityCircle = new google.maps.Circle({
      strokeColor: '#FF0000',
      strokeOpacity: 0.2,
      strokeWeight: 1,
      fillColor: '#FF0000',
      fillOpacity: 0.2,
      map: map,
      center: gateways[gateway].center,
      radius: Math.sqrt(gateways[gateway].radius) * 100
    })
  }
};

        //function addMarker(latlng, map) {
function addMarker(latlng) {
  var marker;
  marker = new google.maps.Marker({
    position: latlng,
    map: map
    })
}; 
