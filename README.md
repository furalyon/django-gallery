==================
Django Gallery App
==================


A simple django app to handle a gallery with albums and pictures. Generates a list page with albums and a detail page for albums with the pictures in it. Also, features lightbox view of images inside an album when clicked.


Pre-requisites
==============
    1) This was built for Python 3.x
    2) Django 1.10+
    3) easy_thumbnails to shrink images before storing (https://github.com/SmileyChris/easy-thumbnails)
    4) MEDIA_URL, MEDIA_ROOT setup for your django project (https://docs.djangoproject.com/en/1.10/howto/static-files/#serving-files-uploaded-by-a-user-during-development)


Installation
============

Download a copy of the gallery app folder in the repo and put it in your project folder.

Add ``gallery`` to your ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        ...
        'gallery',
    )


Initial setup
=============

In your main ``urls.py`` add::

    url(r'^gallery/', include('gallery.urls', namespace='gallery')),

Migrate database::

    python manage.py migrate



settings.py
-----------

    THUMBNAIL_ALIASES = {
        '': {
            'photo': {'size': (500, 500), 'crop': True},
        },
    }

    # 1.25MB - 1310720
    # 2.5MB - 2621440
    # 5MB - 5242880
    # 10MB - 10485760
    # 20MB - 20971520
    # 50MB - 5242880
    # 100MB 104857600
    # 250MB - 214958080
    # 500MB - 429916160
    MAX_PHOTO_SIZE = 10485760
    MAX_PHOTO_COUNT = 1000

base.html
---------

Add gallery list page to your main menu

    <a href="{% url 'gallery:list' %}">Gallery</a>

Usage
=====

Now, you can add photos using admin section and they will displayed on the public gallery pages.