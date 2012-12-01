uwaterlooapi README
===================

Thin Python wrapper for the University of Waterloo Open Data API. The API is documented here: http://api.uwaterloo.ca/

Installing
----------


Using pip::

   pip install requests
   pip install -e hg+ssh://hg@bitbucket.org/amjoconn/shad#egg=shad
   pip install -e hg+https://bitbucket.org/amjoconn/uwaterlooapi#egg=uwaterlooapi

Usage
-----
  
Basic usage::

    >>> from uwaterlooapi import UWaterlooAPI
    >>> uw = UWaterlooAPI(api_key="YOUR API KEY")
    >>> uw.weather()
    {u'Date': u'04-01-2012', u'Current': {u'Windchill': u'NA', u'Temp': u'4.1', u'Min': u'2.6', u'Max': u'7.9', u'Radiation': u'77.8', u'Humidity': u'100', u'WindDir': u'NE', u'Wind': u'0', u'AsOf': u'2:15 PM', u'Precipitation': u'2.6', u'Day': u'Today', u'Condition': u'Light rain', u'Icon': u'http://www.google.com/ig/images/weather/mist.gif'}, u'Week': {u'Sun': {u'High': u'9', u'Image': u'http://www.google.com/ig/images/weather/chance_of_rain.gif', u'Low': u'-2', u'Condition': u'Chance of Rain'}, u'Wed': {u'High': u'12', u'Image': u'http://www.google.com/ig/images/weather/sunny.gif', u'Low': u'-3', u'Condition': u'Clear'}, u'Mon': {u'High': u'12', u'Image': u'http://www.google.com/ig/images/weather/sunny.gif', u'Low': u'-2', u'Condition': u'Clear'}, u'Tue': {u'High': u'13', u'Image': u'http://www.google.com/ig/images/weather/mostly_sunny.gif', u'Low': u'2', u'Condition': u'Partly Sunny'}}}

By default a method returns a Python dictionary of the contents of the data section of the full JSON response.

Generally I used the documenation names for methods as the Python method names, with a few exceptions for clarity::

    >>> dir(uw)
    ['OMGUW', '__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_register', 'api_key', 'buildings', 'calendar_events', 'course_info', 'course_rerequisites', 'course_schedule', 'course_search', 'daily_events', 'departments_list', 'exam_schedule', 'faculties_list', 'food_menu', 'food_services_info', 'parking', 'professor_details', 'professor_search', 'programs_list', 'publication_details', 'recent_publications', 'staff_info', 'terms_list', 'university_holidays', 'url', 'vending_machines_list', 'watcard_vendors_list', 'watpark', 'weather']

Most arguments are passed in as keywords::

    >>> uw.watpark(output="JSON")
    '{"response":{"meta":{"Requests":"0","Timestamp":"2012-04-01T14:45:27-04:00","Status":"200","Message":"OK","Version":"1.4b5"},"data":{"result":[{"ID":"1","LotName":"C","LatLong":"43.467536,-80.538379","OpenTime":"6 a.m.","CloseTime":"3 a.m.","LatestCount":"220","TimePolled":"2012-04-01 14:44:50","Capacity":"807","PercentFilled":"27"},{"ID":"5","LotName":"N","LatLong":"43.47491,-80.544559","OpenTime":"6 a.m.","CloseTime":"3 a.m.","LatestCount":"0","TimePolled":"","Capacity":"-1","PercentFilled":"0"},{"ID":"6","LotName":"W","LatLong":"43.474777,-80.547579","OpenTime":"6 a.m.","CloseTime":"3 a.m.","LatestCount":"0","TimePolled":"","Capacity":"-1","PercentFilled":"0"},{"ID":"7","LotName":"X","LatLong":"43.477526,-80.545492","OpenTime":"6 a.m.","CloseTime":"3 a.m.","LatestCount":"0","TimePolled":"","Capacity":"-1","PercentFilled":"0"}]}}}'

Explicitly setting output type caused method to return unparsed strings in the provide output type.

An common exception are q argument which can be positional or keyword::

    >>> uw.staff_info("lwsmith")
    {u'Name': u'Larry Smith', u'Office': u'HH 146', u'UserID': u'lwsmith', u'Phone': u'519-888-4567 x32647', u'Department': u'Economics', u'Email': u'lwsmith@uwaterloo.ca'}

A final example with printing XML::

    >>> print uw.terms_list(output="xml")
    <?xml version="1.0" encoding="UTF-8"?>
    <response>
            <meta>
                    <Requests>2</Requests>
                    <Timestamp>2012-04-01T14:45:46-04:00</Timestamp>
                    <Status>200</Status>
                    <Message>OK</Message>
                    <Version>1.4b5</Version>
            </meta>
            <data>
                    <Current>1121</Current>
                    <result>
                            <ID>1109</ID>
                            <Name>Fall</Name>
                            <Year>2010</Year>
                    </result>
                    <result>
                            <ID>1111</ID>
                            <Name>Winter</Name>
                            <Year>2011</Year>
                    </result>
                    <result>
                            <ID>1115</ID>
                            <Name>Spring</Name>
                            <Year>2011</Year>
                    </result>
                    <result>
                            <ID>1119</ID>
                            <Name>Fall</Name>
                            <Year>2011</Year>
                    </result>
                    <result>
                            <ID>1121</ID>
                            <Name>Winter</Name>
                            <Year>2012</Year>
                    </result>
                    <result>
                            <ID>1125</ID>
                            <Name>Spring</Name>
                            <Year>2012</Year>
                    </result>
                    <result>
                            <ID>1129</ID>
                            <Name>Fall</Name>
                            <Year>2012</Year>
                    </result>
            </data>
    </response>
