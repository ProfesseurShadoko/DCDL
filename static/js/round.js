
//where are the divs we need to hide
const cards_div = $(".my-card").parent();
const target_div = cards_div[0];
const cards = []

function hideCards() {
    cards_div.css("visibility","hidden");
}

//what are the grid positions where cards will be displayed ?
function findCards(cards_char) {
    const start = Math.floor((10-cards_char.length)/2);
    for (i=0; i<cards_char.length; i++) {
        cards.push(cards_div[i+start+1]);
    }
}


function writeCards() {
    for (i=0; i<cards.length; i++) {
        $(cards[i]).children().html(cards_char[i]);
    }

    $(target_div).children().html(target);
}

function getCard(i) {
    return cards[i];
}

function show(card) {
    $(card).css("visibility","visible");
}
