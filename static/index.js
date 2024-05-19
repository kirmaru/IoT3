
function Lighting(){
    $.ajax({
        type: 'GET',
        url: '/light',
        dataType: 'json',
        contentType: 'application/json',
        data: {
            "value": document.getElementById("lum").value
        },
        success: function(response){
            document.getElementById("lum").value = response.lum; // Update lum value
            document.getElementById("power").value = response.power; // Update power value
            document.getElementById("avg_lum").value = response.avg_lum; // Update average lum value
            document.getElementById("max_lum").value = response.max_lum; // Update maximum lum value
        }
    });
}
function Climate(){
    $.ajax({
    type: 'GET',
    url: '/climate',
    dataType: 'json',
    contentType: 'application/json',
    data: {
        "humid": document.getElementById("humid").value,
        "temp": document.getElementById("temp").value
    },
    success: function(response){
        document.getElementById("humid").value = response.humid;
        document.getElementById("temp").value = response.temp;
    }
    })
}

function DoorStatus(){
    $.ajax({
    type: 'GET',
    url: '/doors',
    dataType: 'json',
    contentType: 'application/json',
    data: {
        "value": document.getElementById("door_status").value
    },
    success: function(response) {
            document.getElementById("doors").value = response;
        }
    })
}

function create_chart() {
    $.ajax({
        type: 'GET',
        url: '/get_chart',
        dataType: 'json',
        contentType: 'application/json',
        data: {},
        success: function(response) {
            new Chart(
                document.querySelector('.chart'), {
                    type: 'line',
                    data: {
                        labels: response['time_data'],
                        datasets: [{
                            label: 'Освещенность',
                            data: response['lum_data'],
                            cubicInterpolationMode: 'monotone',
                            borderColor: 'rgba(54, 162, 235, 1)',
                            backgroundColor: 'rgba(54, 162, 235, 0.2)',
                            borderWidth: 4,
                            pointBackgroundColor: 'rgba(54, 162, 235, 1)',
                            pointBorderColor: '#fff',
                            pointHoverBackgroundColor: '#fff',
                            pointHoverBorderColor: 'rgba(54, 162, 235, 1)',
                            pointRadius: 7,
                            pointHoverRadius: 10
                        }]
                    },
                    options: {
                        responsive: true,
                        plugins: {
                            legend: {
                                position: 'bottom',
                                labels: {
                                    font: {
                                        size: 16,
                                        family: 'Arial',
                                        style: 'italic',
                                        weight: 'bold'
                                    },
                                    color: '#333'
                                }
                            },
                            title: {
                                display: true,
                                text: 'График освещенности',
                                font: {
                                    size: 24,
                                    family: 'Arial',
                                    style: 'normal',
                                    weight: 'bold'
                                },
                                color: '#333'
                            }
                        },
                        scales: {
                            x: {
                                display: true,
                                title: {
                                    display: true,
                                    text: 'Время',
                                    font: {
                                        size: 18,
                                        family: 'Arial',
                                        style: 'normal',
                                        weight: 'bold'
                                    },
                                    color: '#333'
                                },
                                ticks: {
                                    color: '#333',
                                    font: {
                                        size: 14
                                    }
                                },
                                grid: {
                                    display: true,
                                    color: 'rgba(200, 200, 200, 0.2)'
                                }
                            },
                            y: {
                                display: true,
                                title: {
                                    display: true,
                                    text: 'Освещенность (люкс)',
                                    font: {
                                        size: 18,
                                        family: 'Arial',
                                        style: 'normal',
                                        weight: 'bold'
                                    },
                                    color: '#333'
                                },
                                ticks: {
                                    color: '#333',
                                    font: {
                                        size: 14
                                    }
                                },
                                grid: {
                                    display: true,
                                    color: 'rgba(200, 200, 200, 0.2)'
                                }
                            }
                        }
                    }
                }
            );
        }
    });
}

