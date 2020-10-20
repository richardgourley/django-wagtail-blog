from django import template
from wagtail.core.models import Site

register = template.Library()
'''
See base.html to see where we call {% load home_menu %} (the name of this file) to load this template tag
After loading we can call {% get_menu %} (function below)
which then passes data to and display "tags/navbar.html"
'''
@register.inclusion_tag("tags/navbar.html")
def get_menu():
	site = Site.objects.get(is_default_site=True)
	home_page = site.root_page
	pages = homePage.get_children().live().in_menu()
	return {
	    "home_page":home_page,
	    "pages":pages,
	}