$ = django.jQuery;
var userProfile = {
		
    init:function(){
    	
    	$("#social a").unbind().bind('click', function(){
    		var redirect_uri = 'http://myalbumshare.com:8000/users/userprofile/auth'
    		var url = 'https://www.facebook.com/dialog/oauth?client_id=113400205406273&redirect_uri='+redirect_uri+'&response_type=token';
    		
    		var token;
    		var socialNetwork = $(this).attr('id');
    		console.log(socialNetwork);
    		
    		popupWindow = window.open(url,"_blank","toolbar=no, location=yes, directories=no, status=no, scrollbars=no, resizable=no, width=400, height=400, top=200, left=250");
    		
    		var watchClose = setInterval(function() {
    		    if (popupWindow.closed) {
    		    	clearTimeout(watchClose);
    		    	userProfile._populateToken(socialNetwork);
    		    }
    		 }, 200);
    		
    		return false;
    	});
    },
    
    _populateToken:function(socialNetwork){
    	var json = JSON.parse($("#id_tokens").attr('value'));
    	json[socialNetwork] = $.cookie('mss');
    	
    	$("#id_tokens").attr('value',JSON.stringify(json));
    }
};

$(document).ready(function() {
	userProfile.init()
});