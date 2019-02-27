#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Sitio web
SITENAME = 'Consejo de Participación Ciudadana del Sistema Anticorrupción del Estado de Coahuila de Zaragoza'
SITEURL = 'http://www.cpccoahuila.org.mx'
SITELOGO = 'imagenes/coahuila.png'
SITEDESCRIPTION = ''
SITETWITTER = '@cpccoahuila'

# Autor por defecto
AUTHOR = 'CPC Coahuila'

# Directorio donde esta el contenido
PATH = 'content'

# Directorios que tienen las publicaciones
ARTICLE_PATHS = ['comunicados', 'documentos']

# Directorios que tienen páginas, no publicaciones
PAGE_PATHS = ['3de3', 'consejeros', 'contacto', 'transparencia']

# Directorios y archivos que son fijos
# Agregue también los directorios con archivos para las artículos
STATIC_PATHS = ['CNAME', 'favicon.ico', 'LICENSE', 'README.md', 'robots.txt',
                '3de3', 'consejeros', 'comunicados', 'documentos']

# Usar el nombre del directorio como la categoría
USE_FOLDER_AS_CATEGORY = True

# Los artículos van en directorios categoria/titulo/
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'

# Las páginas fijas van en directorios categoria/titulo/
PAGE_URL = '{category}/{slug}/'
PAGE_SAVE_AS = '{category}/{slug}/index.html'

# Tema
THEME = 'themes/cpccoahuila-2019-02'
#THEME = 'themes/startbootstrap-clean-blog'

# Encabezados para los autores
AUTHORS_TITLES = { 'cc': 'Comité Coordinador',
                   'comunicados': 'Comunicados',
                   'cpc': 'Consejo de Participación Ciudadana',
                   'general': 'General',
                   'secretaria-ejecutiva': 'Secretaría Ejecutiva', }

# Encabezados para las categorías
CATEGORIES_TITLES = {
    '3de3': '3 de 3',
    'comunicados': 'Comunicados',
    'contacto': 'Contacto',
    'documentos': 'Documentos', }

# Encabezados para las etiquetas
TAGS_TITLES = {'comunicados': 'Comunicados de Prensa',
               'capacitaciones': 'Capacitaciones',
               'comision-ejecutiva': 'Comisión Ejecutiva',
               'comite-coordinador': 'Comité Coordinador',
               'consejo-de-participacion-ciudadana': 'Consejo de Participación Ciudadana',
               'organo-de-gobierno': 'Órgano de Gobierno',
               'presentaciones': 'Presentaciones',
               'reuniones': 'Reuniones',
               'secretaria-ejecutiva': 'Secretaría Ejecutiva',
               'sesiones': 'Sesiones', }

# Lenguaje y zona horaria
DEFAULT_LANG = 'es'
TIMEZONE = 'America/Mexico_City'

# Para desarrollo, los vinculos son relativos
RELATIVE_URLS = True

# Paginacion
DEFAULT_PAGINATION = True
DEFAULT_PAGINATION = 9
DEFAULT_ORPHANS = 2
#DEFAULT_PAGINATION = False

# Usar servicios remotos
USE_REMOTE_SERVICES = True

# Para desarrollo, borrar todo output
DELETE_OUTPUT_DIRECTORY = True

# No eliminar de output los siguientes directorios y archivos
OUTPUT_RETENTION = ['.git', '.gitignore']

# Siempre aprovechar lo que se tenga en caché
LOAD_CONTENT_CACHE = True

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
