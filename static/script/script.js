
// animation on toggle
$(document).ready(
   function(){
        setTimeout(function(){
            $('.navbar-toggler').addClass('shake');
        }, 3000);
    }, function(){
        $('.navbar-toggler').removeClass('shake');
    }
);
//disappear flash massages

setTimeout(function(){
   $("#flash-message").fadeOut();
}, 5000);


window.onload = function() {
    var deleteLinks = document.getElementsByClassName("delete-link");
    for (var i = 0; i < deleteLinks.length; i++) {
        deleteLinks[i].addEventListener("click", function(event) {
            if (!confirm("Are you sure you want to delete this item?")) {
                event.preventDefault();
            }
        });
    }
};

//Print preview
function printpreview(){
    var navbar = document.getElementsByClassName("navbar")[0];
    var body = document.getElementsByTagName('body')[0]
    var header = document.getElementById("cv-header")
    var footer = document.getElementById("cv-footer")
    navbar.style.display = "none";
    footer.style.display = "none";
    body.style.backgroundColor = "white";
    header.style.marginTop = "1rem";

    window.print();
    navbar.style.display = "flex";
    footer.style.display = "block";
    body.style.backgroundColor = "var(--white)";
    header.style.marginTop = "4rem";

}
