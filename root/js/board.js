// make board
// colour = setTimeout(() => {
// 	colour = localStorage.getItem("colour");
// 	if (colour == "b") {
// 		document.getElementById("board").style.transform = "rotate(180deg)";
// 	}
// }, 3000);

setTimeout(function () {
	set_board();
}, 1000);

colour = localStorage.getItem("colour");
if (colour == "b") {
	document.getElementById("board").style.transform = "rotate(180deg)";
}

for (var i = 0; i < 64; i++) {
	a = document.createElement("div");
	a.style.backgroundColor =
		parseInt(i / 8 + i - 1) % 2 == 0 ? "#ababab" : "white";
	a.className = "square";
	letter = "abcdefgh"[i % 8];
	number = 9 - Math.ceil((i + 1) / 8);
	a.id = letter + number;
	a.ondragenter = dragEnter;
	a.ondrop = dragDrop;
	a.ondragover = dragOver;
	document.getElementById("board").appendChild(a);
}

// pieces
function assign(name, e, link, c, id) {
	var piece = document.createElement("div");
	piece.classList.add("piece")
	piece.className = "piece";
	if (colour == "b") {
		piece.style.transform = "rotate(180deg)";
	}
	piece.id = name;
	icon = document.createElement("img");
	icon.src = link;
	icon.className = "piece-img";
	icon.draggable == "false";
	if (colour == c) {
		piece.classList.remove("piece")
		piece.classList.add("own-piece")
	}
	piece.appendChild(icon);
	piece.ondragstart = dragStart;
	piece.ondragend = dragEnd;
	document.getElementById(e).appendChild(piece);
	piece.classList.add(id);
}

function set_board() {
	assign(
		"R",
		"a8",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Chess_rdt45.svg/1024px-Chess_rdt45.svg.png",
		"b"
	);
	assign(
		"N",
		"b8",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Chess_ndt45.svg/1024px-Chess_ndt45.svg.png",
		"b"
	);
	assign(
		"B",
		"c8",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Chess_bdt45.svg/1024px-Chess_bdt45.svg.png",
		"b"
	);
	assign(
		"Q",
		"d8",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Chess_qdt45.svg/800px-Chess_qdt45.svg.png",
		"b"
	);
	assign(
		"K",
		"e8",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Chess_kdt45.svg/800px-Chess_kdt45.svg.png",
		"b"
	);
	assign(
		"B",
		"f8",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Chess_bdt45.svg/1024px-Chess_bdt45.svg.png",
		"b"
	);
	assign(
		"N",
		"g8",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Chess_ndt45.svg/1024px-Chess_ndt45.svg.png",
		"b"
	);
	assign(
		"R",
		"h8",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Chess_rdt45.svg/1024px-Chess_rdt45.svg.png",
		"b"
	);

	assign(
		"",
		"a7",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Chess_pdt45.svg/1024px-Chess_pdt45.svg.png",
		"b"
	);
	assign(
		"",
		"b7",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Chess_pdt45.svg/1024px-Chess_pdt45.svg.png",
		"b"
	);
	assign(
		"",
		"c7",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Chess_pdt45.svg/1024px-Chess_pdt45.svg.png",
		"b"
	);
	assign(
		"",
		"d7",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Chess_pdt45.svg/1024px-Chess_pdt45.svg.png",
		"b"
	);
	assign(
		"",
		"e7",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Chess_pdt45.svg/1024px-Chess_pdt45.svg.png",
		"b"
	);
	assign(
		"",
		"f7",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Chess_pdt45.svg/1024px-Chess_pdt45.svg.png",
		"b"
	);
	assign(
		"",
		"g7",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Chess_pdt45.svg/1024px-Chess_pdt45.svg.png",
		"b"
	);
	assign(
		"",
		"h7",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Chess_pdt45.svg/1024px-Chess_pdt45.svg.png",
		"b"
	);

	assign(
		"R",
		"a1",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Chess_rlt45.svg/1024px-Chess_rlt45.svg.png",
		"w"
	);
	assign(
		"N",
		"b1",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Chess_nlt45.svg/1024px-Chess_nlt45.svg.png",
		"w"
	);
	assign(
		"B",
		"c1",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Chess_blt45.svg/1024px-Chess_blt45.svg.png",
		"w"
	);
	assign(
		"Q",
		"d1",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Chess_qlt45.svg/1024px-Chess_qlt45.svg.png",
		"w"
	);
	assign(
		"K",
		"e1",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Chess_klt45.svg/1024px-Chess_klt45.svg.png",
		"w"
	);
	assign(
		"B",
		"f1",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Chess_blt45.svg/1024px-Chess_blt45.svg.png",
		"w"
	);
	assign(
		"N",
		"g1",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Chess_nlt45.svg/1024px-Chess_nlt45.svg.png",
		"w"
	);
	assign(
		"R",
		"h1",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Chess_rlt45.svg/1024px-Chess_rlt45.svg.png",
		"w"
	);

	assign(
		"",
		"a2",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Chess_plt45.svg/1024px-Chess_plt45.svg.png",
		"w"
	);
	assign(
		"",
		"b2",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Chess_plt45.svg/1024px-Chess_plt45.svg.png",
		"w"
	);
	assign(
		"",
		"c2",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Chess_plt45.svg/1024px-Chess_plt45.svg.png",
		"w"
	);
	assign(
		"",
		"d2",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Chess_plt45.svg/1024px-Chess_plt45.svg.png",
		"w"
	);
	assign(
		"",
		"e2",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Chess_plt45.svg/1024px-Chess_plt45.svg.png",
		"w"
	);
	assign(
		"",
		"f2",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Chess_plt45.svg/1024px-Chess_plt45.svg.png",
		"w"
	);
	assign(
		"",
		"g2",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Chess_plt45.svg/1024px-Chess_plt45.svg.png",
		"w"
	);
	assign(
		"",
		"h2",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Chess_plt45.svg/1024px-Chess_plt45.svg.png",
		"w"
	);
}

document.getElementsByTagName
function change_board(pgn) {
	pieces = document.getElementsByClassName('own-piece')
	for(i=0; i<pieces.length; i++){
		console.log(pieces[i].id)
	}
	console.log(pieces)
}

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
	a = get_token();
	if (a == true && moved_piece.className == 'own-piece') {
		if (this.hasChildNodes()) {
			this.removeChild(this.lastElementChild);
			this.append(moved_piece);
		} else {
			this.append(moved_piece);
		}
		move = moved_piece.id + this.id;
		onmove(move, time, colour);
		// console.log(pgn)
	} else {
		console.log(get_token());
	}
}

function dragOver(e) {
	e.preventDefault();
}
