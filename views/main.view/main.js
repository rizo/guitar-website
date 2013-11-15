

var content = null;

var menu = {
    "home": [],
    "about": [],
    "downloads": [],
    "documentation": []
}


function _init_elements()
{
    // Initialize the content holder element.
    content = document.getElementById("content");

    // Initialize the menu elements.
    Object.keys(menu).forEach(function(id) {
        menu[id].push(document.getElementById(id));
        menu[id].push(document.getElementById(id + "-content"));
        menu[id][0].onclick = function() { load_content(id) };
    });
}

function load_content(id)
{
    content.innerHTML = menu[id][1].innerHTML;
    Object.keys(menu).forEach(function(id) {
        menu[id][0].className = "";
    });
    menu[id][0].className = "active";
}


function init()
{
    _init_elements();
    load_content("home");
}




