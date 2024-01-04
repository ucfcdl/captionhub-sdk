from setuptools import setup, find_packages

setup(
    name='captionhub-sdk',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='University of Central Florida - Learning Systems and Technologies',
    author_email='ahmadaltaher.alfayad@ucf.edu',
    description='Tools for interacting with the CaptionHub API',
    long_description=open('README.md').read(),
)
