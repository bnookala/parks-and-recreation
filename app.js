$(document).ready(function () {
	var map = L.mapbox.map('map', 'bnookala.ia5763g5').setView([37.7833, -122.4167], 12);

	$.getJSON(
		'parks.geojson',
		function (data) {
			map.featureLayer.setGeoJSON(data);
		}.bind(this)
	)
});
