uwaterlooapi README
===================

Thin Python wrapper for version 2 of University of Waterloo Open Data API. The API is documented here: http://api.uwaterloo.ca/

Installing
----------

Using pip::

   pip install uwaterlooapi

Usage
-----

Basic usage::

    >>> from uwaterlooapi import UWaterlooAPI
    >>> uw = UWaterlooAPI(api_key="YOUR API KEY")
    >>> uw.current_weather()
    {u'temperature_24hr_min_c': -24.6, u'wind_speed_kph': 2.1, u'humidex_c': None, u'observation_time': u'2014-03-03T17:15:00-05:00', u'temperature_current_c': -15.7, u'precipitation_24hr_mm': 0, u'wind_direction_degrees': 45, u'elevation_m': 334.4, u'pressure_kpa': 102.8, u'precipitation_1hr_mm': 0, u'temperature_24hr_max_c': -14.6, u'longitude': -80.5576, u'pressure_trend': u'Rising', u'latitude': 43.4738, u'windchill_c': -17.8, u'incoming_shortwave_radiation_wm2': 90.9, u'precipitation_15min_mm': None, u'dew_point_c': -20, u'relative_humidity_percent': 65.1}

By default a method returns a Python dictionary of the contents of the data section of the full JSON response.

Generally I used the documenation names for methods as the Python method names, with a few exceptions for clarity::

    >>> dir(uw)
    [..., 'announcements', 'api_changelog', 'api_key', 'api_methods', 'api_services', 'api_usage', 'api_versions', 'base_url', 'building_list', 'current_weather', 'diets', 'group_codes', 'holidays', 'infosessions', 'instruction_codes', 'locations', 'menu', 'notes', 'outlets', 'printers', 'server_codes', 'server_time', 'subject_codes', 'term_codes', 'terms', 'tutors', 'unit_codes', 'watcard']
