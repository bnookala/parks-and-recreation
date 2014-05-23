$(document).ready(function () {
	var map = L.mapbox.map('map', 'bnookala.ia5763g5').setView([37.7833, -122.4167], 12);
	Parse.initialize("vOfd7H7ltgQUwEqNnZoasBSvXqOErfjUV4LOTIjZ", "vDLTR8myOnupvtQzyX0h3Q4zBwIYjMMiDabRwDbZ");

	$.getJSON(
		'parks_nice.geojson',
		function (data) {
			map.featureLayer.setGeoJSON(data);
		}.bind(this)
	);
});
