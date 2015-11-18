$(document).ready(function(){

$("#nav-btn-container").click(function(){
  	$(this).find('a').toggleClass("open");
  	$("h1").addClass("fade");
});

$("#no-transaction").click(function(){
  $('#loading').show();
  poll();
});

$("#places-btn-container").click(function(){
	if(($(event.target).is($(this))) || ($(event.target).is($(this).find('.places-btn')))){
  	$(".places-container").animate({'top':'0'});
  	$(".places-btn").css('fontsize','18px');
  	$("#close-places-btn").show()
	}
});

$(".close-places-btn-container").click(function(){
    $("#close-places-btn").hide()
  	$(".places-container").animate({'top':$(window).height()-50},500);
  	$(".places-btn").css('fontsize','16px');
});

$(".signup-btn").click(function(){
    $("#main-login").scrollTo('#signup-container',300);
});

$("#back-to-login").click(function(){
    $("#main-login").scrollTo('#login-container',300);
});


})