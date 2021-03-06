$(document).ready(function() {

	//get canvas
	var ctx = $("#line-chartcanvas");

	var data = {
		labels : ["match1", "match2", "match3", "match4", "match5"],
		datasets : [
			{
				label : "TeamA score",
				data : [10, 50, 25, 70, 40],
				backgroundColor : "#b69eee",
				borderColor : "#5e3fbe",
				fill : true,
				lineTension : 0,
				pointRadius : 5
			}
			
		]
	};

	var options = {
		title : {
			display : true,
			position : "top",
			text : "Line Graph",
			fontSize : 18,
			fontColor : "#5e3fbe"
		},
		legend : {
			display : true,
			position : "bottom"
		}
	};

	var chart = new Chart( ctx, {
		type : "line",
		data : data,
		options : options
	} );

});