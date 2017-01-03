import os

# Use setuptools if we can
try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup

packages = [
    'uwaterlooapi',
]

requires = ['shad>=0.1.4']

setup(
    name='uwaterlooapi',
    version='0.3.1',
    description='Thin library wrapper for the University of Waterloo Open Data API.',
    long_description='See http://api.uwaterloo.ca/ for a descripton of the API.',
    author='Albert O\'Connor',
    author_email='info@albertoconnor.ca',
    url='https://bitbucket.org/amjoconn/uwaterlooapi',
    packages=packages,
    package_data={'': ['LICENSE', 'NOTICE']},
    package_dir={},
    include_package_data=True,
    install_requires=requires,
    license='MIT',
    zip_safe=False,
    classifiers=(
        "Development Status :: 3 - Alpha",
        'Intended Audience :: Developers',
        "Operating System :: OS Independent",
    ),

)
