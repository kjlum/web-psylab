#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kim Lum'
SITENAME = u'PSy Lab'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)
SOCIAL = (('Twitter', 'http://twitter.com/talham_'),
    ('Github', 'http://github.com/talha131'))

DEFAULT_PAGINATION = 4

THEME = 'themes/blue-penguin'
SITEURL = 'http://localhost:8000' #TODO: CHANGE THIS
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'
PAGE_ORDER_BY = 'sortorder'
ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}.html'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Elegant recommended variables
PLUGIN_PATHS = ['pelican-plugins/sitemap', 'pelican-plugins/extract_toc', 'pelican-plugins/tipue_search']
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.headerid': {},
        'markdown.extensions.extra': {},
        'markdown.extensions.toc': {'permalink': 'true'},
    },
    'output_format': 'html5',
}
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives'))
STATIC_PATHS = ['theme/images', 'images', 'documents']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''


PROJECTS = [
        {
            'name': 'All Digital DC-DC conversion',
            'url': '/all-digital-dc-dc-conversion',
            'description': 'We are currently working on exploiting the structure '
            'inherent in digital systems to enable all-digital DC-DC buck converter '
            'implementations'},
        {
            'name': 'Quasi-Resonant Clocking',
            'url': '/quasi-resonant-clocking',
            'description': 'Aug 2014: My group introduced Quasi Resonant Clocking. '
            'The technique employs run-time control and optimization to enable, for '
            'the first time, a true voltage-frequency scalable resonant clocking '
            'capability.'},
        {
            'name': 'All Digital Power Supply Measurement',
            'url': '/power-supply-measurement',
            'description': 'Aug, 2014: Kannan Shankaragomathi and William Anthony '
            'Smith presented their work on an all-digital power high-bandwidth '
            'power supply noise measurement system at ISLPED2014'
        }]

LANDING_PAGE_ABOUT = {
    'title': 'About the Group',
    'details': """
    <div itemscope itemtype="http://schema.org/Person">
        <p>Our research is primarily focused on solving important (and interesting) problems in 
        the design and analysis of integrated systems, with a particular emphasis on 
        energy-efficient design.</p>

        <p>Across a wide range of systems, from high-performance servers to energy-scavenging 
        ultra-low power systems, energy dissipation has emerged as a determining factor in 
        performance and design feasibility. Our current goal is to explore minimum energy 
        dissipation limits as we build sophisticated systems in increasingly variable and 
        unreliable process technologies. Applications include high-performance computing, mobile 
        and embedded systems, implantable bio-medical devices, hardware security, and 
        neuro-engineering. Current research focus is on circuit-architecture-system co-design in 
        three main areas:

        <ul>
            <li>Clocking</li>
            <li>Supply conversion, distribution and regulation,</li>
            <li>Ultra low-power sensing, recording, and computation</li>
        </ul>

        <p>In the area of clocking, my group seeks to advance the state-of-the-art in digital 
        system clocking technology.  Current work in the area of clock design includes low-voltage 
        all-digital PLLs, circuits and architectures for next-generation clock distribution, and 
        the exploitation of resonance for ultra-wide DVFS systems throughout the entire clock 
        distribution.</p>

        <p>In the area of power supply conversion, delivery, and regulation, my group is building 
        upon our previous work in the area of clock-stretching for voltage droop mitigation. 
        Research problems involve all-digital DC-DC converters for digital systems, radical 
        regulation architectures for heterogeneous integrated systems and 3D chipstacks, as well 
        as power converters and regulators in ultra-low power systems for biomedical implants.</p>

        <p>We have witnessed the end of Dennard scaling, and continue to see increasing levels of 
        integration in modern designs. Radical gains in performance and efficiency will require 
        the identification, analysis, and exploitation of structure not only across the 
        circuit-architecture-system-application strata, but also across traditionally separated 
        sub-fields. A unique feature of my group is a keen interest and track record in exploiting 
        ideas from diverse fields to provide fresh perspectives and elegant solutions to problems 
        in seemingly unrelated areas. We plan to continue our cross-pollination activities into 
        the future.</p>

        </div>"""}

SLIDESHOW = [
    {
        'src': '/images/All-digital-buck1.jpg',
        'title': 'All Digital DC-DC Converters for Digital Systems',
        'text': 'We are currently working on exploiting the structure inherent in digital systems to enable all-digital DC-DC buck converter implementations',
        'url': '/all-digital-dc-dc-conversion'
    },
    {
        'src': '/images/Picture8.jpg',
        'title': 'Power-Supply Noise Measurement',
        'text': 'Aug, 2014: Kannan Shankaragomathi and William Anthony Smith presented their work on an all-digital power high-bandwidth power supply noise measurement system at ISLPED2014',
        'url': '/power-supply-measurement'
    }
]

CONTACT_INFO = {
    'name': 'Professor Visvesh S. Sathe',
    'email': 'sathe@uw.edu',
    'office_phone': '206-543-7635' 
}
