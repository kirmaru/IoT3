
function DoorStatus(){ //doors
    &.ajax({
    type: 'GET',
    url: '/doors',
    dataType: 'json',
    contentType: 'application/json',
    data: {},
    success: function(response){
        document.getElementById("door_status").value = response["door_status"]
    }
    })
}

function Climate(){
    &.ajax({
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
    &.ajax({
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

