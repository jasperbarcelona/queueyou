$(document).ready(function(){

$("#nav-btn-container").click(function(){
  $(this).find('a').toggleClass("open");
  $("h1").addClass("fade");
});

})