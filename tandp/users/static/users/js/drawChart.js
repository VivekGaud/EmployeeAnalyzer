 console.log("memory_arr")
 console.log(typeof memory_arr)
 console.log(memory_arr)
 // memory_arr = [1,2,3,4]
 console.log("all_process")
 console.log(typeof all_process)
 console.log(all_process)
 all_process = ["Coding", "Documentation", "Internet", "SQL"]

 chart_canvas = document.getElementById("myChart")

var color_array = ['rgba(153, 102, 255, 0.2)','rgba(255, 102, 255, 0.2)','rgba(153, 255, 255, 0.2)']

// function load_chart(chart_type){
//  chart_canvas = document.getElementById("myChart")
//  var drawLineChart = new Chart(chart_canvas, {
//  	  type: chart_type,
//       data: {
//       labels: all_process,
//       datasets: [{
//             label: "chart ",
//             data: memory_arr,
//             backgroundColor:color_array,
//             borderColor:'rgba(255, 159, 64, 1)',
//             borderWidth: 1
//         }]
// },
// options: {
//     	responsive: true,
//     	maintainAspectRatio: false,
//         scales: {
//             yAxes: [{
//                 ticks: {
//                     beginAtZero:true
//                 }
//             }]
//         }
//     }
//  });

// }
// load_chart("line")

// function update_chart(type) {
//     load_chart(type)


var color_array = ['rgba(153, 102, 255, 0.2)','rgba(255, 102, 255, 0.2)','rgba(153, 255, 255, 0.2)','rgba(101, 170, 255, 0.2)']

load_chart = function(chart_type){
 chart_canvas = document.getElementById("myChart")
 var drawLineChart = new Chart(chart_canvas, {
 	  type: chart_type,
      data: {
      labels: all_process,
      datasets: [{
            label: all_process,
            data: memory_arr,
            backgroundColor:color_array,
            borderColor:'rgba(255, 159, 64, 1)',
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

}

load_chart("line");

update_chart = function(type) {
    load_chart(type)
};

