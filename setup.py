
# Use setuptools if we can
try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup

setup(
    name='uwaterlooapi',
    version="0.9.0",
    description='Thin library wrapper for the University of Waterloo Open Data API.',
    long_description='See http://api.uwaterloo.ca/ for a descripton of the API.',
    author='Albert O\'Connor',
    author_email='info@albertoconnor.ca',
    url='https://bitbucket.org/amjoconn/uwaterlooapi',
    download_url='',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
    packages=[
        'uwaterlooapi'
    ],
)
