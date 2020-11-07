move = "";
moved_piece = 0;
pgn = [];

function dragStart() {
	moved_piece = this;
	// console.log(moved_piece)
}

function dragEnd() {}

function dragEnter() {
	move = this.id;
}
function dragDrop() {
	time = 500;
	if (this.hasChildNodes()) {
		this.removeChild(this.lastElementChild);
		this.append(moved_piece);
	} else {
		this.append(moved_piece);
	}
	move = moved_piece.id + this.id;
	onmove(move, time, colour);
	// console.log(pgn)
}

function dragOver(e) {
	e.preventDefault();
}