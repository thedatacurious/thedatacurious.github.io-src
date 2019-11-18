#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = 'Alexandra Khoo'
SITENAME = 'The Data Curious'
SITEURL = 'https://thedatacurious.github.io'
#SITEURL = 'http://localhost:8000'
THEME = './themes/voce'
USER_LOGO_URL = 'https://raw.githubusercontent.com/thedatacurious/thedatacurious.github.io-src/master/content/images/logo.png'

PATH = 'content'
OUTPUT_PATH = '../output'
STATIC_PATHS = ['images', 'extra/favicon.ico']

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

#    'extra/favicon-16x16.png': {'path': 'favicon-16x16.png'},
#    'extra/favicon-32x32.png': {'path': 'favicon-32x32.png'},
#    'extra/android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},
#    'extra/safari-pinned-tab.svg': {'path': 'safari-pinned-tab.svg'},
#    'extra/site.webmanifest': {'path': 'site.webmanifest'},
#    'extra/mstile-150x150.png': {'path': 'mstile-150x150.png'},
#    'extra/apple-touch-icon.png': {'path': 'apple-touch-icon.png'}


PAGE_PATHS = ['pages']

TIMEZONE = 'Asia/Singapore'

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%b %d, %Y'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('About', '/about.html'),
         ('Portfolio', '/portfolio.html'),
         ('Sharing', '/sharing.html'),
         ('Articles', '/index.html')
         )

        
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Email', 'mailto:thedatacurious@gmail.com'),
          ('GitHub', 'http://github.com/thedatacurious'),
	  ('Linkedin', 'https://www.linkedin.com/in/alexandra-khoo-15517557/'),
          ('Medium', 'https://medium.com/@the.data.curious'))

#Page Settings
PAGE_SAVE_AS = '{slug}.html'
#TAGS_URL = 'tags.html'
# ARCHIVES_URL = 'archive.html'
DEFAULT_PAGINATION = False

# Custom settings
MANGLE_EMAILS = True
CURRENT_YEAR = datetime.now().year

# Uncomment following line if you want document-relative URLs when developingi
# RELATIVE_URLS = True
