try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Twitter opinion Mining',
    'author': 'Sarneet Nivranshu Prashant Raveesh',
    'url': 'github',
    'version': '0.1',
    'install _requires': ['nose', 'tweepy'],
    'scripts': [],
    'packages': 'miner',
    'name': 'Major'
}

setup(**config)