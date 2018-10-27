from setuptools import setup, find_packages


setup(
    name='locator_opensky',
    version='0.1.0',
    description='Test task for used and filtration API opensky-network.org',
    author='Ulyantsev Aleksandr',
    author_email='it.bumerang@gmail.com',
    packages=find_packages(),
    url='https://github.com/Bumerang47/locatorOpenSky',
    long_description=open('README.md').read(),
    install_requires=open('requirements.txt').read().splitlines(),
    entry_points={
        'console_scripts': [
            'locator_opensky = locator_opensky.public:__main__'
        ]
    }
)
