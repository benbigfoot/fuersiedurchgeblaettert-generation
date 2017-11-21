# -*- coding: utf-8 -*-
from __future__ import unicode_literals

LOAD_CONTENT_CACHE = False
CACHE_CONTENT = False
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".git"]
IGNORE_FILES = ['__pycache__']
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']

SITEURL = 'http://für-sie-durchgeblättert.de'
RELATIVE_URLS = True

ARTICLE_URL = '{slug}.html'
ARTICLE_SAVE_AS = '{slug}.html'
ARTICLE_LANG_URL = '{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = '{slug}-{lang}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'
ARCHIVES_SAVE_AS = 'archive.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
TAGS_SAVE_AS = 'tags.html'
INDEX_SAVE_AS = 'index.html'
#SLUG_SUBSTITUTIONS = ()
# SLUG_SUBSTITUTIONS = (('C++', 'cpp'), ('keep dot', 'keep.dot', True))
#TAG_SUBSTITUTIONS = ((' ', '_', False))

TIMEZONE = "Europe/Berlin"
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%d %B %Y'
AUTHOR = "Lutz Beister"
DEFAULT_LANG = 'de'

# THEMES !!!

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'images',
	'intern',
    ]

# 

#GOOGLE_ANALYTICS = 
 
#MENUITEMS = (('title', 'url'), ('title', 'url'))
