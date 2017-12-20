from distutils.core import setup

import kontur

setup(
    name='kontur-api',
    version=kontur.__version__,
    description='SKB Kontur API',
    author='Anton Gladkov',
    author_email='anton.gladkov@gmail.com',
    url='http://github.com/agladkov/kontur-api',
    packages=['kontur', 'kontur.focus']
)
