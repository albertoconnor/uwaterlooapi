
import new
import urllib
import json

class UWaterlooAPI(object):
    def __init__(self, api_key=None, url="http://api.uwaterloo.ca/public/v1/"):
        self.api_key = api_key
        self.url = url
        
    @classmethod
    def _register(cls, api_call, name=None):
        method = new.instancemethod(api_call, None, cls)
        if not name: name = api_call.__name__
        setattr(cls, name, api_call)
    
class APIFunction(object):
    method = None
    
    def __init__(self, api, args, kwargs):
        self.api = api
        self.args = args
        self.kwargs = kwargs

        if "output" in kwargs or "callback" in kwargs:
            self.explicit = True
        else:
            self.explicit = False

        self.response = None
    
    def encode(self):
        params = self.kwargs
        # Overwite key and service
        params["key"] = self.api.api_key
        params["service"] = self.method
        if "output" not in params:
            params["output"] = "json"
        return urllib.urlencode(params)
    
    def execute(self):
        if self.method is None:
            raise NotImplementedError, u'Subclass of APIFunction needs to define a valid "method" attribute.'
        
        request = "%s?%s" % (self.api.url, self.encode())
        self.response = urllib.urlopen(request).read()
        if self.explicit:
            return self.response
        else:
            return json.loads(self.response)['response']['data'] # Unwrap automatically         

def binder(function_class):
    closed = function_class
    def _bound(api, *args, **kwargs):
        func = closed(api, args, kwargs)
        return func.execute()
    _bound.__name__ = function_class.__name__
    return _bound

def bind(cls):
    UWaterlooAPI._register(binder(cls))
    return cls

# Geolocation

@bind
class buildings(APIFunction):
    method = "Buildings"

@bind
class parking(APIFunction):
    method = "ParkingList"

@bind
class watpark(APIFunction):
    method = "WatPark"

# Events

@bind
class daily_events(APIFunction):
    method = "Events"

@bind
class calendar_events(APIFunction):
    method = "CalendarEvents"

@bind
class university_holidays(APIFunction):
    method = "Holidays"

# I got tired...

@bind
class weather(APIFunction):
    method = "weather"

