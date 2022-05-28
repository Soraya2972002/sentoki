$(function(){

    //get the doughnut chart canvas
    var ctx1 = $("#doughnut-chartcanvas-1");
    var ctx2 = $("#doughnut-chartcanvas-2");

    //doughnut chart data
    var data1 = {
        labels: ["match1", "match2", "match3", "match4", "match5"],
        datasets: [
            {
                label: "TeamA Score",
                data: [37, 63],
                backgroundColor: [
                    "#DEB887",
                    "#A9A9A9",
                   
                ],
                borderColor: [
                    "#CDA776",
                    "#989898",
                   
                ],
                borderWidth: [1, 1, 1, 1, 1]
            }
        ]
    };

    //doughnut chart data
    var data2 = {
        labels: ["match1", "match2"],
        datasets: [
            {
                label: "TeamB Score",
                data: [37, 63],
                backgroundColor: [
                    "#ba77c7",
                    "#e4d9fa",
                    
                ],
                borderColor: [
                    "#ba77c7",
                    "#e4d9fa",
                   
                ],
                borderWidth: [1, 1, 1, 1, 1]
            }
        ]
    };

    //options
    var options = {
        responsive: true,
        title: {
            display: true,
            position: "top",
            text: "Doughnut Chart",
            fontSize: 18,
            fontColor: "#ba77c7"
        },
        legend: {
            display: true,
            position: "bottom",
            labels: {
                fontColor: "#ba77c7",
                fontSize: 16
            }
        }
    };

    //create Chart class object
    var chart1 = new Chart(ctx1, {
        type: "doughnut",
        data: data1,
        options: options
    });

    //create Chart class object
    var chart2 = new Chart(ctx2, {
        type: "doughnut",
        data: data2,
        options: options
    });
});