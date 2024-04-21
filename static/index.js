
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
    }
    })
}

function Climate(){
    $.ajax({
    type: 'GET',
    url: '/climate',
    dataType: 'json',
    contentType: 'application/json',
    data: {
        "value": document.getElementById("climate").value
    },
    success: function(response){
        document.getElementById("climate").value = response
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



