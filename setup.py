try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Twitter opinion Mining',
    'author': 'Sarneet Nivranshu Prashant Raveesh',
    'url': 'github',
    'version': '0.1',
    'install _requires': ["nose >= 1.3.7", "tweepy >= 3.5.0"],
    'scripts': [],
    'packages': 'miner',
    'name': 'Major'
}

setup(**config)