const piece = document.querySelector(".piece");
const square = document.querySelector(".square");

piece.addEventListener('dragstart', dragStart);
piece.addEventListener('dragend', dragEnd);

function dragStart(){
    // console.log(this.id, this.parentNode.id)
    console.log("start")
}

function dragEnd(){
    // console.log(this.id, this.parentNode.id)
    console.log("stop")
}