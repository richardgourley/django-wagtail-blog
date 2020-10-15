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
				displaySearchResults.innerHTML += i; 
			}
			
		}
    }
})



