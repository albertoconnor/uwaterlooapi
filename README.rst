uwaterlooapi README
===================

Thin Python wrapper for the University of Waterloo Open Data API. The API is documented here: http://api.uwaterloo.ca/

NOTE: This implementation is not yet complete! Adding new methods is easy though.

Installing
----------

Using pip::

   pip install -e hg+https://bitbucket.org/amjoconn/uwaterlooapi#egg=uwaterlooapi

Usage
-----
  
Using Weather as an example::

   >>> from uwaterlooapi import UWaterlooAPI
   >>> api = UWaterlooAPI(api_key="YOUR API KEY HERE")
   >>> api.weather()
   Returns weather json

Any positional or unrecongized keyword arguments will be ignored. If "output" or "callback" keyword arguments are provided the raw response is returned.
