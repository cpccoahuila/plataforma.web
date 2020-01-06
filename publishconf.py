#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# Feed generation
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = None
FEED_ALL_RSS = 'feeds/all.rss.xml'
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

# Feed options
FEED_MAX_ITEMS = 12
RSS_FEED_SUMMARY_ONLY = True

# Para publicar
RELATIVE_URLS = False
LOAD_CONTENT_CACHE = True
DELETE_OUTPUT_DIRECTORY = True

# Paginacion
DEFAULT_PAGINATION = True
DEFAULT_PAGINATION = 9
DEFAULT_ORPHANS = 2

# Path to the folder containing the plugins
PLUGIN_PATHS = ['plugins']

# The plugins you want to be enabled
PLUGINS = ['sitemap']

# Configuration for the "sitemap" plugin
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1,
        'indexes': 0.5,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'always',
        'indexes': 'hourly',
        'pages': 'daily'
    },
    'exclude': [
        'archives.html',
        'tags.html',
        'categories.html',
        'author/',
        'category/',
        'tag/']
}

# Usar servicios remotos
USE_REMOTE_SERVICES = True
