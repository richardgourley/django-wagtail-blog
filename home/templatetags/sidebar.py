from django import template
from blog.models import BlogPage

register = template.Library()

@register.inclusion_tag("tags/sidebar.html")
def get_sidebar():
	blogpages = BlogPage.objects.live().order_by('-first_published_at')
	return {
	    "blogpages":blogpages,
	}