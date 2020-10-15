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

/*
console.log(test_data);

var app = new Vue({
  delimiters: ["[[", "]]"],
  el: '#app',
  data: {
    message: 'Hello Richard!'
  }
})

var app2 = new Vue({
	el: '#app2',
	data: {
		message: 'You loaded this page on ' + new Date().toLocaleString()
	}
})

var app3 = new Vue({
	el: '#app3',
	data: {
		seen: true
	}
})

var app4 = new Vue({
	delimiters: ["[[", "]]"],
	el: '#app4',
	data: {
		todos: [
		  { text: 'javascript' },
		  { text: 'python' },
		  { text: 'kotlin'}
		]
	}
})

app4.todos.push({ text:'c#'});

var app5 = new Vue({
	delimiters: ["[[", "]]"],
	el: "#app5",
	data: {
		message: 'NOEL ELLIOTT GOURLEY'
	},
	methods: {
		reverseMessage: function(){
			this.message = this.message.split('').reverse().join('')
		}
	}
})

var app6 = new Vue({
    delimiters: ["[[", "]]"],
    el: '#app6',
    data: {
      message: 'Hello Vue!'
    }
})

Vue.component('todo-item',{
	props: ['todo'],
	template: '<li>{{ todo.text }}</li>'

})

var app7 = new Vue({
	el: '#app7',
	data: {
		groceryList: [
            { id:0, text: 'Vegetables'},
            { id:1, text: 'Cheese'},
            { id:2, text: 'Whatever else...'},
		]
	}
})

*/


