
function search() {
    console.log('searh!')
    let term = $('#search_input').val()
    if(term !== '') {
        $.ajax({
            type: "GET",
            headers: {"Content-Type":  "application/json", 
                      "Access-Control-Allow-Origin": "*"},
            url: "/search"

        }).done( function( data ) {
            console.log(data)
            $( ".result" ).html( data.senteces );
        });

    }
} 

$('#search_button').click(search)
