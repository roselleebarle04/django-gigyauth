import os
from distutils.command.install import INSTALL_SCHEMES
from distutils.core import setup
import gigyauth

setup(
    name = 'django-gigyauth',
    version = gigyauth.get_version(),
    packages =  ['gigyauth'], 
    description = 'Connect to all social networks with gigyauth',
    url = 'http://code.google.com/p/django-gigyauth/',
)
