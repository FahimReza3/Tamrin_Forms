
$("#Karbord-img").click(function() {
    $(".Modal").fadeToggle();
});

function Data( id , FullName , Email , Password){

    $("#id_id").val(id)
    $("#id_FullName").val(FullName)
    $("#id_Email").val(Email)
    $("#id_Password").val(Password)

}