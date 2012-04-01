
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
    arg_names = [] # name for positional arguments. If more arguments are provided then there are names they are ignored.
    
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
            
        if len(self.arg_names) > len(self.args):
            raise TypeError, "%s requires %s arguments (%s given)" % (self.__class__.__name__, len(self.arg_names), len(self.args))
            
        for name, arg in zip(self.arg_names, self.args):
            params[name] = str(arg)
            
        return urllib.urlencode(params)
    
    def execute(self):
        if self.method is None:
            raise NotImplementedError, u'Subclass of APIFunction needs to define a valid "method" attribute.'
        
        request = "%s?%s" % (self.api.url, self.encode())
        self.response = urllib.urlopen(request).read()
        if self.response == "": # This happens when you search for something and there are no results, should probably be an empty list instead...
            return None
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

@bind
class course_search(APIFunction):
    """
    course_search(q) where q is a string like "CS 241"
    """
    method = "CourseSearch"
    arg_names = ["q"]

@bind
class course_info(APIFunction):
    """
    course_info(q) where q is a string like "CS 241"
    """
    method = "CourseInfo"
    arg_names = ["q"]

@bind
class course_rerequisites(APIFunction):
    """
    course_rerequisite(q) where q is a string like "CS 241"
    """
    method = "Prerequisites"
    arg_names = ["q"]

@bind
class faculties_list(APIFunction):
    method = "FacultiesList"
    
@bind
class departments_list(APIFunction):
    method = "DepartmentsList"
    
@bind
class terms_list(APIFunction):
    method = "TermsList"

@bind
class exam_schedule(APIFunction):
    method = "ExamSchedule"
    
@bind
class food_services_info(APIFunction):
    method = "FoodServices"
    
@bind
class food_menu(APIFunction):
    method = "FoodMenu"
    
@bind
class vending_machines_list(APIFunction):
    method = "VendingMachines"
    
@bind
class watcard_vendors_list(APIFunction):
    method = "WatcardVendors"

@bind
class professor_search(APIFunction):
    """
    professor_search(q) where q is a string like "conrad"
    """
    method = "ProfessorSearch"
    arg_names = ["q"]
   
@bind
class professor_details(APIFunction):
    """
    professor_details(q) where q a rate my professor id like "9845"
    """
    method = "ProfessorDetails"
    arg_names = ["q"] 

@bind
class programs_list(APIFunction):
    method = "ProgramsList"

@bind
class recent_publications(APIFunction):
    method = "RecentPublications"


@bind
class publication_details(APIFunction):
    """
    publication_details(q) where q a publication ID "6030"
    """
    method = "PublicationDetails"
    arg_names = ["q"] 

@bind
class course_schedule(APIFunction):
    """
    course_schedule(q, term=current_term) where q a publication ID "6030" and term is a term id like "1119".
    Term needs to be specified as a keyword argument
    """
    method = "Schedule"
    arg_names = ["q"] 

@bind
class weather(APIFunction):
    method = "weather"

@bind
class staff_info(APIFunction):
    """
    staff_info(q) where q a WATIAM username like "lwsmith"
    """
    method = "StaffInfo"
    arg_names = ["q"] 

@bind
class OMGUW(APIFunction):
    method = "OMGUW"