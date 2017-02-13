try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Twitter opinion Mining',
    'author': 'Sarneet Nivranshu Prashant Raveesh',
    'url': 'github',
    'version': '0.1',
    'install_requires': ["nose >= 1.3.7", "tweepy >= 3.5.0" , "pymongo >= 2.3.0", "requests >= 2.13.0", "botornot >= 0.3"],
    'scripts': [],
    'packages': ['miner','major_mongo'],
    'name': 'Major'
}

setup(**config)