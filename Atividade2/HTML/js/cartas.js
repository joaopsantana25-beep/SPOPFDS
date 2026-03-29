
let rand=0
const cartas=document.getElementsByClassName('card')
let playerx
let numer,coni=0





 function rdmcard() {
    
    for (let index = 0; index < cartas.length; index++) {
        cartas[index].addEventListener('click', function() {
            cartas[index].style.transform = 'rotateY(180deg)';
        });
    }
    for (let index = 0; index < cartas.length; index++) {
        cartas[index].style.display='none'
    }
    rand = Math.floor((Math.random()*cartas.length))
    cartas[rand].style.display="block"
    cartas[rand].style.animation="flip 1s"
    let carta = cartas[rand]
    document.addEventListener('keypress', function(event) {
        if (event.code === 'Space') {
            carta.remove()
            rdmcard()
        }  
    });
 }

 