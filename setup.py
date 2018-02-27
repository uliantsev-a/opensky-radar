from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='locator_opensky',
    version='1.1',
    description='Test task for used and filtration API opensky-network.org',
    packages=find_packages(),
    install_requires=[ 'requests', ],
    url='https://github.com/Bumerang47/locatorOpenSky',
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    entry_points={
        'console_scripts': [
            'locator_opensky = locator_opensky._public:__main__'
        ]
    }
)