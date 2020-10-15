// Get django data variable
let blogPosts = JSON.parse(document.getElementById('blogPostsJSON').textContent);
//String to objects
let parsedBlogPosts = JSON.parse(blogPosts);

//output div for search results
let displaySearchResults = document.getElementById('displaySearchResults');

var app6 = new Vue({
    delimiters: ["[[", "]]"],
    el: '#blogSearchInput',
    data: {
      message: 'Welcome'
    },
    methods: {
    	searchPosts: function(){
    		displaySearchResults.innerHTML = "";
			for(i=0; i<parsedBlogPosts.length; i++){
				if((parsedBlogPosts[i].title).indexOf(this.message) > -1){
					displaySearchResults.innerHTML += '<div class="p-3">';
					displaySearchResults.innerHTML += "<h4>" + parsedBlogPosts[i].title + "</h4>";
					displaySearchResults.innerHTML += "<small>Date: " + parsedBlogPosts[i].date + "</small>";
					displaySearchResults.innerHTML += '<p><a href="' + parsedBlogPosts[i].url + '">Read</a></p>';
					displaySearchResults.innerHTML += '</div>';
				}
			}
			if(displaySearchResults.innerHTML == ""){
				displaySearchResults.innerHTML = '<div class="p-3"><h3>Sorry. Nothing Found</h3>';
			}
			
		}
    }
})



