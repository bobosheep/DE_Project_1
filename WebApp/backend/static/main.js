
function search() {
    let term = $('#search_input').val()
    if(term !== '') {
        console.log('search ' + term)
        $.ajax({
            url: "/search",
            data: { term: term, page: "1"},
            type: 'GET'
        }).done( function( data ) {
            console.log(data)
            let htmlstr = ''
            for(let i = 0 ; i < data.sentences.length ; i++) {
                htmlstr += '<div class="notification">' + data.sentences[i].name + '</div>'
            }
            $( ".result" ).html(htmlstr);
        });

    }
} 

$('#search_button').click(search)
$('#search_input').keyup(function(event) {
    if(event.key === 'Enter'){
        search()
    }
})
