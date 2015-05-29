from setuptools import setup, find_packages

setup(
    name = 'django-news-sitemaps',
    version = '0.1.7',
    description = 'Generates sitemaps compatible with the Google News schema',
    author = 'TWT Web Devs',
    author_email = 'webdev@washingtontimes.com',
    url = 'http://github.com/washingtontimes/django-news-sitemaps/',
    package_data = {'': ['templates/**/*']},
    packages = find_packages(exclude=('example',)),
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
    ]
)
