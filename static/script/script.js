
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
