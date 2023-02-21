function preventBack() {
    window.history.forward();
}
setTimeout("preventBack()", 0);
window.onunload = function () {
    window.location.href = "/";
};


function search() {
    var search, filter, table, tr, td, i, txtVal;
    search = document.getElementById("searchbx");
    filter = search.value.toUpperCase();
    table = document.getElementById("voter");
    tr = table.getElementsByTagName("tr");
    for (i = 1; i < tr.length; i++) {
        td = tr[i];
        if (td) {
            txtVal = td.textContent || td.innerText;
            if (txtVal.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}

function search2() {
    var search, filter, table, tr, td, i, txtVal;
    search = document.getElementById("searchbx2");
    filter = search.value.toUpperCase();
    table = document.getElementById("candidate");
    tr = table.getElementsByTagName("tr");
    for (i = 1; i < tr.length; i++) {
        td = tr[i];
        if (td) {
            txtVal = td.textContent || td.innerText;
            if (txtVal.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}

function search3() {
    var search, filter, table, tr, td, i, txtVal;
    search = document.getElementById("searchbx3");
    filter = search.value.toUpperCase();
    table = document.getElementById("results");
    tr = table.getElementsByTagName("tr");
    for (i = 1; i < tr.length; i++) {
        td = tr[i];
        if (td) {
            txtVal = td.textContent || td.innerText;
            if (txtVal.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}

function hide_show_table(col_name) {
    var button_val = document.getElementById(col_name).value;
    if (button_val == "hide") {
        var all_col = document.getElementsByClassName(col_name);
        for (var i = 0; i < all_col.length; i++) {
            all_col[i].style.display = "none";
        }
        document.getElementById(col_name + "_head").style.display = "none";
        document.getElementById(col_name).value = "show";
    }

    else {
        var all_col = document.getElementsByClassName(col_name);
        for (var i = 0; i < all_col.length; i++) {
            all_col[i].style.display = "table-cell";
        }
        document.getElementById(col_name + "_head").style.display = "table-cell";
        document.getElementById(col_name).value = "hide";
    }
}