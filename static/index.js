
function Lighting(){
    $.ajax({
    type: 'GET',
    url: '/light',
    dataType: 'json',
    contentType: 'application/json',
    data: {},
    success: function(response){
        document.getElementById("lum").value = response["lum"]
    }
    })
}

function Climate(){
    $.ajax({
    type: 'GET',
    url: '/climate',
    dataType: 'json',
    contentType: 'application/json',
    data: {},
    success: function(response){
        document.getElementById("climate").value = response["climate"]
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
            if (response.length > 0) {
                document.getElementById("doors").value = response;
            } else {
                document.getElementById("doors").value = "No doors connected";
            }
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



