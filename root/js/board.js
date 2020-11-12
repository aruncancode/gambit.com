// make board
// colour = setTimeout(() => {
// 	colour = localStorage.getItem("colour");
// 	if (colour == "b") {
// 		document.getElementById("board").style.transform = "rotate(180deg)";
// 	}
// }, 3000);

setTimeout(function () {
	set_board();
}, 200);

// pieces
function assign(name, e, link, c, id) {
	var piece = document.createElement("div");
	if (colour == "b") {
		piece.style.transform = "rotate(180deg)";
	}
	piece.id = name;
	icon = document.createElement("img");
	icon.src = link;
	icon.className = "piece-img";
	icon.draggable == "false";
	if (colour == c) {
		piece.classList.add("own-piece");
	} else {
		piece.classList.add("piece");
	}
	piece.appendChild(icon);
	piece.ondragstart = dragStart;
	piece.ondragend = dragEnd;
	document.getElementById(e).appendChild(piece);
	piece.classList.add(id);
}

function set_board() {
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

	assign(
		"R",
		"a8",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Chess_rdt45.svg/1024px-Chess_rdt45.svg.png",
		"b",
		"ROOKB1"
	);
	assign(
		"N",
		"b8",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Chess_ndt45.svg/1024px-Chess_ndt45.svg.png",
		"b",
		"KNIGHTB1"
	);
	assign(
		"B",
		"c8",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Chess_bdt45.svg/1024px-Chess_bdt45.svg.png",
		"b",
		"BISHOPB1"
	);
	assign(
		"Q",
		"d8",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Chess_qdt45.svg/800px-Chess_qdt45.svg.png",
		"b",
		"QUEENB"
	);
	assign(
		"K",
		"e8",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Chess_kdt45.svg/800px-Chess_kdt45.svg.png",
		"b",
		"KINGB"
	);
	assign(
		"B",
		"f8",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Chess_bdt45.svg/1024px-Chess_bdt45.svg.png",
		"b",
		"BISHOPB2"
	);
	assign(
		"N",
		"g8",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Chess_ndt45.svg/1024px-Chess_ndt45.svg.png",
		"b",
		"KNIGHTB2"
	);
	assign(
		"R",
		"h8",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Chess_rdt45.svg/1024px-Chess_rdt45.svg.png",
		"b",
		"ROOKB2"
	);

	assign(
		"a",
		"a7",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Chess_pdt45.svg/1024px-Chess_pdt45.svg.png",
		"b",
		"PAWNBA"
	);
	assign(
		"b",
		"b7",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Chess_pdt45.svg/1024px-Chess_pdt45.svg.png",
		"b",
		"PAWNBB"
	);
	assign(
		"c",
		"c7",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Chess_pdt45.svg/1024px-Chess_pdt45.svg.png",
		"b",
		"PAWNBC"
	);
	assign(
		"d",
		"d7",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Chess_pdt45.svg/1024px-Chess_pdt45.svg.png",
		"b",
		"PAWNBD"
	);
	assign(
		"e",
		"e7",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Chess_pdt45.svg/1024px-Chess_pdt45.svg.png",
		"b",
		"PAWNBE"
	);
	assign(
		"f",
		"f7",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Chess_pdt45.svg/1024px-Chess_pdt45.svg.png",
		"b",
		"PAWNBF"
	);
	assign(
		"g",
		"g7",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Chess_pdt45.svg/1024px-Chess_pdt45.svg.png",
		"b",
		"PAWNBG"
	);
	assign(
		"h",
		"h7",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Chess_pdt45.svg/1024px-Chess_pdt45.svg.png",
		"b",
		"PAWNBH"
	);

	assign(
		"R",
		"a1",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Chess_rlt45.svg/1024px-Chess_rlt45.svg.png",
		"w",
		"ROOKW1"
	);
	assign(
		"N",
		"b1",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Chess_nlt45.svg/1024px-Chess_nlt45.svg.png",
		"w",
		"KNIGHTW1"
	);
	assign(
		"B",
		"c1",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Chess_blt45.svg/1024px-Chess_blt45.svg.png",
		"w",
		"BISHOPW1"
	);
	assign(
		"Q",
		"d1",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Chess_qlt45.svg/1024px-Chess_qlt45.svg.png",
		"w",
		"QUEENW"
	);
	assign(
		"K",
		"e1",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Chess_klt45.svg/1024px-Chess_klt45.svg.png",
		"w",
		"KINGW"
	);
	assign(
		"B",
		"f1",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Chess_blt45.svg/1024px-Chess_blt45.svg.png",
		"w",
		"BISHOPW2"
	);
	assign(
		"N",
		"g1",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Chess_nlt45.svg/1024px-Chess_nlt45.svg.png",
		"w",
		"KNIGHTW2"
	);
	assign(
		"R",
		"h1",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Chess_rlt45.svg/1024px-Chess_rlt45.svg.png",
		"w",
		"ROOKW2"
	);

	assign(
		"a",
		"a2",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Chess_plt45.svg/1024px-Chess_plt45.svg.png",
		"w",
		"PAWNWA"
	);
	assign(
		"b",
		"b2",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Chess_plt45.svg/1024px-Chess_plt45.svg.png",
		"w",
		"PAWNWB"
	);
	assign(
		"c",
		"c2",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Chess_plt45.svg/1024px-Chess_plt45.svg.png",
		"w",
		"PAWNWC"
	);
	assign(
		"d",
		"d2",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Chess_plt45.svg/1024px-Chess_plt45.svg.png",
		"w",
		"PAWNWD"
	);
	assign(
		"e",
		"e2",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Chess_plt45.svg/1024px-Chess_plt45.svg.png",
		"w",
		"PAWNWE"
	);
	assign(
		"f",
		"f2",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Chess_plt45.svg/1024px-Chess_plt45.svg.png",
		"w",
		"PAWNWF"
	);
	assign(
		"g",
		"g2",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Chess_plt45.svg/1024px-Chess_plt45.svg.png",
		"w",
		"PAWNWG"
	);
	assign(
		"h",
		"h2",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Chess_plt45.svg/1024px-Chess_plt45.svg.png",
		"w",
		"PAWNWH"
	);
}

function change_board(pgn) {
	square = document.getElementById(pgn[0]);
	piece = document.getElementsByClassName(pgn[1])[0];
	if (square.hasChildNodes()) {
		square.removeChild(square.lastElementChild);
		square.append(piece);
	} else {
		square.append(piece);
	}
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
	if (a == true && moved_piece.classList.contains("own-piece")) {
		if (this.hasChildNodes()) {
			this.removeChild(this.lastElementChild);
			this.append(moved_piece);
			move = moved_piece.id + this.id;
			if (JSON.stringify(moved_piece.classList).includes("PAWN")) {
				moved_piece.id = this.id[0];
				console.log(moved_piece.id)
			}
		} else {
			this.append(moved_piece);
			move = moved_piece.id + this.id;
			if (JSON.stringify(moved_piece.classList).includes("PAWN")) {
				move = this.id;
			}
		}
		onmove(move, time, colour);
		// console.log(pgn)
	} else {
		console.log(get_token());
	}
}

function dragOver(e) {
	e.preventDefault();
}
