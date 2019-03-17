var memory_arr
console.log(memory_arr)
memory_double_arr = []
memory_double_arr.push(memory_arr)
var all_process
console.log(all_process)

chart_canvas = document.getElementById("SIH")

var myChart = new Chart(chart_canvas, {
    type: 'line',
    data: {
        labels: all_process,
        datasets: [{
            label: 'Memory use of process',
            data: memory_arr,
            backgroundColor:'rgba(153, 102, 255, 11)',
            // backgroundColor: [
            //     'rgba(255, 99, 132, 0.2)',
            //     'rgba(54, 162, 235, 0.2)',
            //     'rgba(255, 206, 86, 0.2)',
            //     'rgba(75, 192, 192, 0.2)',
            //     'rgba(153, 102, 255, 0.2)',
            //     'rgba(255, 159, 64, 0.2)'
            // ],
            // borderColor:'rgba(255, 159, 64, 1)',
            // borderColor: [
            //     'rgba(255,99,132,1)',
            //     'rgba(54, 162, 235, 1)',
            //     'rgba(255, 206, 86, 1)',
            //     'rgba(75, 192, 192, 1)',
            //     'rgba(153, 102, 255, 1)',
            //     'rgba(255, 159, 64, 1)'
            // ],
            borderWidth: 1
        }]
    },
    options: {
    	responsive: true,
    	maintainAspectRatio: false,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }]
        }
    }
});
chart_canvas = document.getElementById("chart2")

var myChart = new Chart(chart_canvas, {
    type: 'bar',
    data: {
        labels: all_process,
        datasets: [{
            label: 'Custom Label',
            data: memory_arr,
            backgroundColor:'rgba(75, 192, 192, 1)',
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }]
        }
    }
});