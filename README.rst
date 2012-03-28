uwaterlooapi README
===================

Thin Python wrapper for the University of Waterloo Open Data API. The API is documented here: http://api.uwaterloo.ca/

NOTE: This implementation is not yet complete! But adding new methods is easy.

Install
-------

Using pip::

pip install -e hg+https://bitbucket.org/amjoconn/uwaterlooapi

Usage
-----
  
Using Weather as an example::

>>> from uwaterlooapi import UWaterlooAPI
>>> api = UWaterlooAPI(api_key="YOU API KEY HERE")
>>> api.weather()
Returns weather json

Any positional or unrecongized keyword arguments will be ignored. If "output" or "callback" keyword arguments are provided the raw response is returned.
