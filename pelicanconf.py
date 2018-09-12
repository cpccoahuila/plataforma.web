#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Sitio web
SITENAME = 'Consejo de Participación Ciudadana del Sistema Anticorrupción del Estado de Coahuila de Zaragoza'
SITEURL = 'http://www.cpccoahuila.org.mx'
SITELOGO = 'imagenes/coahuila.png'
SITEDESCRIPTION = ''

# Autor por defecto
AUTHOR = 'SEA Coahuila'

# Directorio donde esta el contenido
PATH = 'content'

# Directorios que tienen las publicaciones
ARTICLE_PATHS = ['comunicados', 'documentos']

# Directorios que tienen páginas, no publicaciones
PAGE_PATHS = ['3de3', 'contacto', 'transparencia']

# Directorios y archivos que son fijos
# Agregue también los directorios con archivos para las artículos
STATIC_PATHS = ['CNAME', 'favicon.ico', 'imagenes', 'LICENSE', 'README.md',
                '3de3', 'comunicados', 'documentos']

# Usar el nombre del directorio como la categoría
USE_FOLDER_AS_CATEGORY = True

# Los artículos van en directorios categoria/titulo/
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'

# Las páginas fijas van en directorios categoria/titulo/
PAGE_URL = '{category}/{slug}/'
PAGE_SAVE_AS = '{category}/{slug}/index.html'

# Tema
THEME = 'themes/startbootstrap-clean-blog'
#THEME = 'themes/startbootstrap-clean-blog-colores'

# Lenguaje y zona horaria
DEFAULT_LANG = 'es'
TIMEZONE = 'America/Mexico_City'

# Borrar toda la salida,
# Borra directorios ocultos en output como .git, mantenga en falso
DELETE_OUTPUT_DIRECTORY = False

# Para desarrollo, los vinculos son relativos
RELATIVE_URLS = True

# Para desarrollo, se desactiva la paginacion
DEFAULT_PAGINATION = False

# Feed generation
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

# Para desarrollo, recomendado mantener en falso
LOAD_CONTENT_CACHE = False
