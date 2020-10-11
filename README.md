# Django Wagtail Blog

This is an implementation of the Wagtail CMS 'first website' guide on the Wagtail website documentation.

The setup of a Wagtail project is very similar to a normal django application set up.  
See https://wagtail.io/

## EXTRA FEATURES:

1. Bootstrap - downloaded and added the bootstrap 4 .scss files to allow changing the colors and fonts with variables (see packages used below).
2. Menu - incorporated a simple menu using Wagtail page hierarchy and a bootstrap menu.
3. VueJS - added Vue for use on a dynamic blog search page. 

Instead of creating a SPA and setting up a REST API, I only wanted to implement Vue.js with a few pages in the application, rather than setting up a SPA with a REST API.

I also wanted to see if it was possible to use Bootstrap SCSS variables for easily changing the color scheme of the blog as well as using the Bootstrap grid system to create a modern blog.


## DEPENDENCIES
These commands were used after the installation to install dependencies:
1. pip install python-decouple
- See settings/base.py and the file .env to see where this is used. (Ideal for not displaying Secret keys or database log in information in version control.  Make sure you use GITIGNORE to ignore the .env file!)
- https://pypi.org/project/python-decouple/
2. pip install django_compressor
3. pip install django-libsass
- You can see how {% compress css %} is used to process the link to our bootstrap.scss file, in the home_page.html template.
- django-libsass is used to pre-compile the scss to css.
- See settings/base.py to see how they are set up in INSTALLED APPS, STATICFILES_FINDERS and COMPRESS_PRECOMPILERS







