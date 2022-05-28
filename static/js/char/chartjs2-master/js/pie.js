$(document).ready(function () {

	var ctx1 = $("#pie-chartcanvas-1");
	var ctx2 = $("#pie-chartcanvas-2");

	var data1 = {
		labels : ["Alger", "Bejaia", "Tizi Ouzou", "Tipaza", "Guelma"],
		datasets : [
			{
				label : "TeamA score",
				data : [10, 50, 25, 70, 40],
				backgroundColor : [
		           "#5e3fbe",
		          "#a88deb",
		          "#cbb6f8",
		          "#e5dafb",
		          "#f4f0fd"
		                ],
                borderColor : [
                    "#5e3fbe",
			          "#a88deb",
			          "#cbb6f8",
			          "#e5dafb",
			          "#f4f0fd"
                ],
                borderWidth : [1, 1, 1, 1, 1]
			}
		]
	};

	var data2 = {
		labels : ["match1", "match2", "match3", "match4", "match5"],
		datasets : [
			{
				label : "TeamB score",
				data : [20, 35, 40, 60, 50],
				backgroundColor : [
                    "#FAEBD7",
                    "#DCDCDC",
                    "#E9967A",
                    "#F5DEB3",
                    "#9ACD32"
                ],
                borderColor : [
                    "#E9DAC6",
                    "#CBCBCB",
                    "#D88569",
                    "#E4CDA2",
                    "#89BC21"
                ],
                borderWidth : [1, 1, 1, 1, 1]
			}
		]
	};

	var options = {
		title : {
			display : true,
			position : "top",
			text : "Students by Wilaya",
			fontSize : 18,
			fontColor : "#5e3fbe"
		},
		legend : {
			display : true,
			position : "bottom"
		}
	};


	var chart1 = new Chart( ctx1, {
		type : "pie",
		data : data1,
		options : options
	});

	var chart2 = new Chart( ctx2, {
		type : "pie",
		data : data2,
		options : options
	});

});