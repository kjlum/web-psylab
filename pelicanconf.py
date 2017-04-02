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

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Elegant recommended variables
PLUGIN_PATHS = ['pelican-plugins/sitemap', 'pelican-plugins/extract_toc', 'pelican-plugins/tipue_search']
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404', 'research'))
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

RESEARCH_PAGE_OVERVIEW = [
    {
        'title': 'Next-Generation Clocking',
        'id': 'next-gen',
        'details': """
        <p>The past three decades have seen dramatic shifts and transitions in the design of CMOS 
        digital integrated circuits, including the “frequency-race”, increasing variability in 
        advanced process technologies, low-voltage operation, and the design of 3D heterogeneous 
        complexes. With the exception of resonant clocking, there have been few significant changes 
        in the state-of-the-art in system clocking. Clock distributions transitioned from clock 
        planes (high performance) to clock trees (lower power) and back to coarse clock meshes (in 
        response to process variability).</p>

        <img src="/images/res_clk.png" style="margin:0 auto;display:block;" width="397" height="268"/>
        <p style="text-align:center;font-style:italic;">Simplified schematic of a quasi-resonant 
        clocking system</p>

        <p>Today, several new challenges have emerged in the area of clocking including:</p>
        <ul>
            <li>Low-voltage operation, to near-threshold and sub-threshold voltages</li>
            <li>DVFS systems with wide tuning ranges</li>
            <li>Mitigating the impact of supply noise, especially di/dt</li>
            <li>Synchronization and domain crossing between across multiple clock domains in 
            heterogeneous systems</li>
            <li>The increasing difficulty of analog design techniques for clock generation</li>
            <li>3D integration</li>
        </ul>

        <p>
            Previous selected publications in the area:
            <a href="http://vlsi.ee.washington.edu/files/2014/09/resonant_clock_design_for_a_power_efficient_high_volume_x86-64_microprocessor_isscc.pdf">
                [ISSCC]
            </a>
            <a href="http://vlsi.ee.washington.edu/files/2014/09/resonant_clock_design_for_a_power_efficient_high_volume_x86-64_microprocessor.pdf">
                [JSSC]
            </a>
            <a href="http://vlsi.ee.washington.edu/files/2014/09/quasi_resonant_clocking_a_runtime_control_aproach_for_true_voltage_frequency_scaling.pdf">
                [ISLPED]
            </a>
            <a href="https://www.google.com/patents/US20140062566">
                [Pat1]
            </a>
            <a href="https://www.google.com/patents/US8742817">
                [Pat2]
            </a>
        </p>"""
    },
    {
        'title': 'Current problems in clocking',
        'id': 'problems',
        'details': """
        <p>The grounds-up research effort in this area focuses on radically different clocking 
        circuits and architectures which effectively address these myriad challenges. The group is 
        currently focused on:</p>

        <il>
            <li>Low-voltage all-digital PLL design</li>
            <li>Elastic clocking techniques for highly variable and resistive technologies</li>
            <li>Clock distributions for ultra-wide-range DVFS systems</li>
            <li>Greedy synchronization for efficient clock domain crossing for future micro-regulated 
            voltage domains</li>
            <li>Voltage-Frequency scalable clock distribution networks (global and local)</li>
        </il>

        <img src="/images/elastic_clk.png" style="margin:0 auto;display:block;" width="598" height="246"/>
        <p style="text-align:center;font-style:italic;">An elastic clock distribution for efficient, 
        robust clocking</p>"""
    },
    {
        'title': 'Power conversion, distribution and regulation',
        'id': 'power-dist-reg',
        'details': """
        <p>Few areas in IC design are as pervasive and challenging as the analysis and design of power 
        supply systems. The progress of clock rates to beyond package resonance frequencies, the 
        efficiency-driven push for larger number of on-chip voltage domains, reduced form factors 
        in electronic systems, power transfer, conversion and regulation for energy-harvesting 
        systems and even challenges in hardware security have all  driven advances in this field.</p>

        <img src="/images/buck_converter.png" style="margin:0 auto;display:block;" width="597" height="195"/>
        <p style="text-align:center;font-style:italic;">All-digital DC-DC conversion for energy-efficient 
        microprocessors</p>

        <p>We are interested in a number of problems in this area:</p>

        <il>
            <li>Novel voltage regulation techniques and architectures</li>
            <li>Analysis, optimization and design of power front-ends for energy-harvesting applications</li>
            <li>Analysis of supply noise in high performance systems</li>
            <li>Power delivery and regulation in 3D silicon</li>
            <li>Analysis and optimization of voltage regulators for bio-implantable systems</li>
        </il>

        <img src="/images/interlocked_osc.jpg" style="margin:0 auto;display:block;" width="300" height="248"/>
        <p style="text-align:center;font-style:italic;">A novel system to enable fast, all-digital low-dropout 
        regulators for micro-regulated voltage domains.</p>

        <p>
            Previous selected publications in the area:
            <a href="https://www.google.com/patents/US20120187991">
                [Pat1]
            </a>
            <a href="https://www.google.com/patents/US8373512">
                [Pat2]
            </a>
            <a href="http://vlsi.ee.washington.edu/files/2014/10/Deterministic-Dither.pdf">
                [ISLPED]
            </a>
            <a href="http://vlsi.ee.washington.edu/files/2014/09/a_32nm_fully_integrated_reconfigurable_switched_capacitor_dc_dc_converter_delivering_0.55_at_81_efficiency.pdf">
                [ISSCC1]
            </a>
            <a href="http://vlsi.ee.washington.edu/files/2014/10/clock_stretcher_isscc.pdf">
                [ISSCC2]
            </a>
        </p>"""
    }]


