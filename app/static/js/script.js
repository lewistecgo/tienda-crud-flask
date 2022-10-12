$(document).ready(function () {

    function load(query) {
//        var query = $("#requestSearch").val();
        console.log("query: ", query);
        var parametros = {"action": "ajax", 'query': query};
//        $("#loader").fadeIn('slow');
        $.ajax({
            url: '/products',
            type: 'POST',
            data: parametros,
            // beforeSend: function (objeto) {
            //     $("#loader").html("Cargando...");
            // },
            success: function (data) {
                console.log(data.htmlresponse);
                $('#result').html(data.query);
//                $("#result").append(data.htmlresponse);
//                            $(".outer_div").html(data).fadeIn('slow');
//                            $("#loader").html("");
            }
        });
    }

    $("#requestSearch").keyup(function () {
        var search = $(this).val();
        if (search != '') {
            load(search);
        } else {
            load();
        }

    });

});


function reload(){
    document.getElementById('requestSearch').value='';
//    load();

}

