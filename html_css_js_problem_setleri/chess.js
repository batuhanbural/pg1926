document.addEventListener('DOMContentLoaded', function () {
    // Create rows
    for (let i = 1; i < 10; i++) {
        const div = document.createElement("div");
        div.id = "row" + i;
        document.body.appendChild(div)
    }

    // Create Notation
    const chars = ["a", "b", "c", "d", "e", "f", "g", "h"];
    const last_row = document.getElementById("row9");
    for (let i = 0; i < 8; i++) {
        const char_div = document.createElement("div");
        char_div.className = "char square"
        char_div.innerText = chars[i]
        last_row.appendChild(char_div)
    }

    // Add squares
    for (let i = 1; i < 9; i++) {
        const row = document.getElementById("row" + i);
        if (i % 2 === 0) {
            create_squares(row, 1)
            var last_div = document.createElement("div")
            last_div.className = "num square"
            last_div.innerText = "" + (9 - i)
            row.appendChild(last_div)
        } else {
            create_squares(row, 0)
            var last_div = document.createElement("div")
            last_div.className = "num square"
            last_div.innerText = "" + (9 - i)
            row.appendChild(last_div)
        }
    }
}, false);


// Create Squares
function create_squares(row, start = 0) {
    for (let i = 1; i < 5; i++) {
        var w_square = document.createElement("div");
        w_square.id = "white_s" + i;
        w_square.className = "white square";

        var b_square = document.createElement("div");
        b_square.id = "black_s" + i;
        b_square.className = "black square";

        if (start === 0) {
            row.appendChild(w_square);
            row.appendChild(b_square);
        } else {
            row.appendChild(b_square);
            row.appendChild(w_square);
        }

    }
}
