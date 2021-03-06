#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read().strip()
DEPENDENCIES = [
    'distribute',
    'PasteScript>=1.3',
    'Cheetah',
    'fabric',
]


setup(
    name = 'flask-project-templates',
    version = '0.3',
    description = 'Paster templates for creating Flask projects',
    long_description = README,
    author = 'Don Spaulding II',
    author_email = 'donspauldingii@gmail.com',
    url = 'https://github.com/donspaulding/flask-project-templates',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data = True,
    zip_safe = False,
    license = 'GPL',
    keywords = 'flask paster template',
    install_requires = DEPENDENCIES,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Software Development :: Code Generators',
    ],
    entry_points = """
    [paste.paster_create_template]
    flask_basic=flask_project_templates.flasktemplates:FlaskBasicTemplate
    flask_bootstrap=flask_project_templates.flasktemplates:FlaskBootstrapTemplate
    flask_sqla=flask_project_templates.flasktemplates:FlaskSQLAlchemyTemplate
    """,
)
