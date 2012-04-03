$ = django.jQuery;
var userProfile = {
		
    init:function(){
    	
    	$("#social a").unbind().bind('click', function(){
    		var socialNetwork = $(this).attr('id');
    		
    		var redirect_uri = 'http://myalbumshare.com:8000/users/userprofile/auth';

    		var params = {'urls':{
    							'facebook':'https://www.facebook.com/dialog/oauth?',
    							'gplus':'https://accounts.google.com/o/oauth2/auth?scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile&state=%2Fprofile&'
    							},
    					 'client_id':{
    						 'facebook':'113400205406273',
    						 'gplus':'205845695739-juvl4ruak4faa3qrpk5qn95cos12dbi8.apps.googleusercontent.com'
    					 		}
    					};
    		
    		    		
    		//var url_fb = 'client_id=113400205406273&redirect_uri='+redirect_uri+'&response_type=token';
    		
    		//var url_gplus = 'client_id=205845695739-juvl4ruak4faa3qrpk5qn95cos12dbi8.apps.googleusercontent.com&redirect_uri='+redirect_uri+'&response_type=token'
    		
    		var token;
    		
    		var url = params.urls[socialNetwork] + 'client_id=' + params.client_id[socialNetwork] + '&redirect_uri=' + redirect_uri + '&response_type=token';
    		
    		console.log(url);
    		
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