
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


/*
function GaragePassword(){
    &.ajax({
        type: 'GET',
        url: '/PasswordInput',
        dataType: 'json',
        contentType: 'application/json',
        data: {},
        success: function(response){
        document.getElementById("value").value = response["value"]
        }
    })
}
*/