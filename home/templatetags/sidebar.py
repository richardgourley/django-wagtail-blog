from django import template
from blog.models import BlogPage

register = template.Library()

'''
We can call {% load sibebar %} in other pages(the name of this file) to call this template tag
After loading, we can call {% get_sidebar %} corresponding to function below..
.. which passes the data to and displays "tags/sidebar.html"
'''
@register.inclusion_tag("tags/sidebar.html")
def get_sidebar():
    '''
    Gets all blog pages and 'unique' tags used with our blog pages...
    which we use in our sidebar menu - "tags/sidebar.html"
    '''
    blog_tags = set()
    blog_pages = BlogPage.objects.live().order_by('-first_published_at')
    for page in blog_pages:
        for tag in page.tags.all():
            blog_tags.add(tag)
    
    return {
        "blog_pages":blog_pages,
        "blog_tags":blog_tags,
    }