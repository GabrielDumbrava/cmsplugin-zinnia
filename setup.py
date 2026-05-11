"""Setup script for cmsplugin_zinnia"""
from setuptools import setup
from setuptools import find_packages

import cmsplugin_zinnia

setup(
    name='cmsplugin_zinnia',
    version=cmsplugin_zinnia.__version__,

    description='Django-CMS plugins for django-blog-zinnia',
    long_description=open('README.rst').read(),

    keywords='django, blog, weblog, zinnia, cms, plugins, apphook',

    author=cmsplugin_zinnia.__author__,
    author_email=cmsplugin_zinnia.__email__,
    url=cmsplugin_zinnia.__url__,

    packages=find_packages(exclude=['demo_cmsplugin_zinnia']),
    classifiers=[
        'Framework :: Django',
        'Framework :: Django :: 5.2',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'],

    python_requires='>=3.10',
    license=cmsplugin_zinnia.__license__,
    include_package_data=True,
    zip_safe=False,
    install_requires=['Django>=5.2',
                      'django-cms>=5.0',
                      'django-blog-zinnia>=0.20']
)
