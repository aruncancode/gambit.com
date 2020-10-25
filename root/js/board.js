// make board

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
function assign(name, e, link) {
	var piece = document.createElement("div");
	piece.className = "piece";
	piece.id = name;
	icon = document.createElement("img");
	icon.src = link;
	icon.className = "piece-img";
	piece.appendChild(icon);
	icon.draggable = "true";
	piece.ondragstart = dragStart;
	piece.ondragend = dragEnd;
	document.getElementById(e).appendChild(piece);
}


move = ""
moved_piece = 0;
pgn =[]

function dragStart() {
    moved_piece = this
    // console.log(moved_piece)
}

function dragEnd() {
}

function dragEnter() {
	move = this.id;
}
function dragDrop() {
	if (this.hasChildNodes()) {
        this.removeChild(this.lastElementChild);
        this.append(moved_piece)
	} else {
		this.append(moved_piece);
    }
    move = moved_piece.id + this.id
    pgn.push([move])
    console.log(pgn)
}

function dragOver(e) {
	e.preventDefault();
}

assign(
	"R",
	"a8",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Chess_rdt45.svg/1024px-Chess_rdt45.svg.png"
);
assign(
	"N",
	"b8",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Chess_ndt45.svg/1024px-Chess_ndt45.svg.png"
);
assign(
	"B",
	"c8",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Chess_bdt45.svg/1024px-Chess_bdt45.svg.png"
);
assign(
	"Q",
	"d8",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Chess_qdt45.svg/800px-Chess_qdt45.svg.png"
);
assign(
	"K",
	"e8",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Chess_kdt45.svg/800px-Chess_kdt45.svg.png"
);
assign(
	"B",
	"f8",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Chess_bdt45.svg/1024px-Chess_bdt45.svg.png"
);
assign(
	"N",
	"g8",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Chess_ndt45.svg/1024px-Chess_ndt45.svg.png"
);
assign(
	"R",
	"h8",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Chess_rdt45.svg/1024px-Chess_rdt45.svg.png"
);

assign(
	"",
	"a7",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Chess_pdt45.svg/1024px-Chess_pdt45.svg.png"
);
assign(
	"",
	"b7",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Chess_pdt45.svg/1024px-Chess_pdt45.svg.png"
);
assign(
	"",
	"c7",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Chess_pdt45.svg/1024px-Chess_pdt45.svg.png"
);
assign(
	"",
	"d7",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Chess_pdt45.svg/1024px-Chess_pdt45.svg.png"
);
assign(
	"",
	"e7",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Chess_pdt45.svg/1024px-Chess_pdt45.svg.png"
);
assign(
	"",
	"f7",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Chess_pdt45.svg/1024px-Chess_pdt45.svg.png"
);
assign(
	"",
	"g7",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Chess_pdt45.svg/1024px-Chess_pdt45.svg.png"
);
assign(
	"",
	"h7",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Chess_pdt45.svg/1024px-Chess_pdt45.svg.png"
);

assign(
	"R",
	"a1",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Chess_rlt45.svg/1024px-Chess_rlt45.svg.png"
);
assign(
	"N",
	"b1",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Chess_nlt45.svg/1024px-Chess_nlt45.svg.png"
);
assign(
	"B",
	"c1",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Chess_blt45.svg/1024px-Chess_blt45.svg.png"
);
assign(
	"Q",
	"d1",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Chess_qlt45.svg/1024px-Chess_qlt45.svg.png"
);
assign(
	"K",
	"e1",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Chess_klt45.svg/1024px-Chess_klt45.svg.png"
);
assign(
	"B",
	"f1",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Chess_blt45.svg/1024px-Chess_blt45.svg.png"
);
assign(
	"N",
	"g1",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Chess_nlt45.svg/1024px-Chess_nlt45.svg.png"
);
assign(
	"R",
	"h1",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Chess_rlt45.svg/1024px-Chess_rlt45.svg.png"
);

assign(
	"",
	"a2",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Chess_plt45.svg/1024px-Chess_plt45.svg.png"
);
assign(
	"",
	"b2",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Chess_plt45.svg/1024px-Chess_plt45.svg.png"
);
assign(
	"",
	"c2",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Chess_plt45.svg/1024px-Chess_plt45.svg.png"
);
assign(
	"",
	"d2",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Chess_plt45.svg/1024px-Chess_plt45.svg.png"
);
assign(
	"",
	"e2",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Chess_plt45.svg/1024px-Chess_plt45.svg.png"
);
assign(
	"",
	"f2",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Chess_plt45.svg/1024px-Chess_plt45.svg.png"
);
assign(
	"",
	"g2",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Chess_plt45.svg/1024px-Chess_plt45.svg.png"
);
assign(
	"",
	"h2",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Chess_plt45.svg/1024px-Chess_plt45.svg.png"
);