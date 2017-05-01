from setuptools import setup, find_packages

setup(
    name='SusanStatComp',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Implementation of scalable k-means++',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/susancherry/Statistical_Computation.git',
    author='Susan Cherry',
    author_email='susan.cherry@duke.edu'
)
