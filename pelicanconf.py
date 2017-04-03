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
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

THEME = 'themes/elegant-psylab'
SITEURL = 'http://localhost:8000' #TODO: CHANGE THIS
PAGE_URL = '{slug}.html'

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
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''


PROJECTS = [
        {
            'name': 'All Digital DC-DC conversion',
            'url':
            'http://oncrashreboot.com/research/all-digital-dc-dc-conversion',
            'description': 'We are currently working on exploiting the structure '
            'inherent in digital systems to enable all-digital DC-DC buck converter '
            'implementations'},
        {
            'name': 'Quasi-Resonant Clocking',
            'url':
            'http://oncrashreboot.com/research/quasi-resonant-clocking',
            'description': 'Aug 2014: My group introduced Quasi Resonant Clocking. '
            'The technique employs run-time control and optimization to enable, for '
            'the first time, a true voltage-frequency scalable resonant clocking '
            'capability.'},
        {
            'name': 'All Digital Power Supply Measurement',
            'url':
            'http://oncrashreboot.com/research/power-supply-measurement',
            'description': 'Aug, 2014: Kannan Shankaragomathi and William Anthony '
            'Smith presented their work on an all-digital power high-bandwidth '
            'power supply noise measurement system at ISLPED2014'
        }]

LANDING_PAGE_ABOUT = {
    'title': 'Processing Systems Lab',
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

TOC_PAGES = [
    'Research'
]

TOC = {
    'Research': [
        {
            'title': 'Next-Generation Clocking',
            'id': 'next-generation-clocking'
        },
        {
            'title': 'Current problems in clocking',
            'id': 'current-problems-in-clocking'
        },
        {
            'title': 'Power conversion, distribution and regulation',
            'id': 'power-conversion-distribution-and-regulation'
        },
        {
            'title': 'Neural-signal acquisition and processing',
            'id': 'neural-signal-acquisition-and-processing'
        },
        {
            'title': 'Other Research Projects',
            'id': 'other-research-projects'
        }
    ]
}
