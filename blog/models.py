from django import forms
from django.db import models

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet

from json import dumps

# Create your models here.

@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, 
        on_delete=models.SET_NULL, related_name="+"
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('icon')
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'blog categories'

class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        blogpage1 = blogpages[0]
        blogpage2 = blogpages[1]
        blogpage3 = blogpages[2]
        context['blogpage1'] = blogpage1
        context['blogpage2'] = blogpage2
        context['blogpage3'] = blogpage3
        context['blogpages'] = blogpages
        return context

class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name = 'tagged_items',
        on_delete=models.CASCADE
    )

# Even though this is a page without fields, inheriting from 'Page' makes it part of ecosystem

class BlogTagIndexPage(Page):
    def get_context(self, request):
        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context

class BlogSearchPage(Page):
    def get_context(self, request):
        blogPostList = []
        blogPosts = BlogPage.objects.all()
        for post in blogPosts:
            postDict = {}
            postDict["title"] = post.title
            postDict["date"] = str(post.date)
            postDict["url"] = post.url
            blogPostList.append(postDict)

        blogPostsJSON = dumps(blogPostList)
        context = super().get_context(request)
        context['blogPostsJSON'] = blogPostsJSON
        
        return context

class BlogPage(Page):
    date = models.DateField("Post Date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body')
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            # Use widget argument to change from default select box to checkbox
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="Blog Information"),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', label="Gallery images")
    ]

# Orderable adds a sort_order field to the model - allows image sorting
class BlogPageGalleryImage(Orderable):
    # Parental Key is like a Foreign Key
    # Parental Key to BlogPage is what attaches gallery image to a specific page
    # Also defines BlogPageGalleryImage as a child of the BlogPage
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name="gallery_images")
    # image is a foreign key to wagtails built-in image where image is stored
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        # related to image - is a pop up interface for an image chooser panel
        # effectively we have created a many to many relationship between pages and images
        ImageChooserPanel('image'),
        FieldPanel('caption')
    ]



