

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

function Automate_lights(){
    $.ajax({
    type: 'GET',
    url: '/doors',
    dataType: 'json',
    contentType: 'application/json',
    data: {
        "status": document.getElementById("lights_state").value
    },
    success: function(response) {
            document.getElementById("lights_state").value = response;
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
            document.getElementById("lum").value = response
            updateLightCondition(response, document.getElementById("lum").value)
        }
    });
}

function updateLightCondition(response, lum){
    $.ajax({
        type: 'GET',
        url: '/light',
        dataType: 'json',
        contentType: 'application/json',
        data: {
            "light_condition": response["light_condition"],
            "lum": lum
        },
        success: function(response){
            document.getElementById("light_condition").value = response["light_condition"]
        }
    });
}
