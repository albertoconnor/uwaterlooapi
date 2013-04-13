# Use setuptools if we can
try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup

packages = [
    'uwaterlooapi',
]

requires = ['shad']

setup(
    name='uwaterlooapi',
    version='0.2.1',
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
    dependency_links = [
        'https://bitbucket.org/amjoconn/shad/get/default.tar.gz#egg=shad-dev',
    ],
    license='MIT',
    zip_safe=False,
    classifiers=(
        "Development Status :: 3 - Alpha",
        'Intended Audience :: Developers',
        "Operating System :: OS Independent",
    ),

)
