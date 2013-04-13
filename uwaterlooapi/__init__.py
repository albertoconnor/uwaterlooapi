__version__ = '0.2.1'

from shad import BaseAPI, APIFunction, get_bind


class UWaterlooAPI(BaseAPI):
    def __init__(self, api_key=None, base_url='http://api.uwaterloo.ca/public/v1/'):
        self.api_key = api_key
        self.base_url = base_url
    
    def _update_parameters(self, params):
        params["key"] = self.api_key
        if 'output' not in params:
            params['output'] = 'json'
        
        return params
    
    def _process_json(self, data):
        if 'response' in data:
            ret_data = data['response']['data']
        else:
            ret_data = data['data']
        if ret_data is not None and 'result' in ret_data:
            return ret_data['result']
        else:
            return ret_data


class UWaterlooAPIFunction(APIFunction):
    service = None
    
    def _get_parameters(self):
        self.kwargs["service"] = self.service
        return super(UWaterlooAPIFunction, self)._get_parameters()
    
    
bind = get_bind(UWaterlooAPI)


# Geolocation

@bind
class buildings(UWaterlooAPIFunction):
    path  = '/'
    service = "Buildings"

@bind
class building_coordinates(UWaterlooAPIFunction):
    path = '/'
    service = "BuildingCoordinates"

@bind
class parking(UWaterlooAPIFunction):
    path  = '/'
    service = "ParkingList"

@bind
class watpark(UWaterlooAPIFunction):
    path  = '/'
    service = "WatPark"

# Events

@bind
class daily_events(UWaterlooAPIFunction):
    path  = '/'
    service = "Events"

@bind
class calendar_events(UWaterlooAPIFunction):
    path  = '/'
    service = "CalendarEvents"

@bind
class university_holidays(UWaterlooAPIFunction):
    path  = '/'
    service = "Holidays"

@bind
class course_search(UWaterlooAPIFunction):
    """
    course_search(q) where q is a string like "CS 241"
    """
    path  = '/'
    service = "CourseSearch"
    arg_names = ["q"]

@bind
class course_info(UWaterlooAPIFunction):
    """
    course_info(q) where q is a string like "CS 241"
    """
    path  = '/'
    service = "CourseInfo"
    arg_names = ["q"]

@bind
class course_prerequisites(UWaterlooAPIFunction):
    """
    course_rerequisite(q) where q is a string like "CS 241"
    """
    path  = '/'
    service = "Prerequisites"
    arg_names = ["q"]

@bind
class faculties_list(UWaterlooAPIFunction):
    path  = '/'
    service = "FacultiesList"
    
@bind
class departments_list(UWaterlooAPIFunction):
    path  = '/'
    service = "DepartmentsList"
    
@bind
class terms_list(UWaterlooAPIFunction):
    path  = '/'
    service = "TermsList"

@bind
class exam_schedule(UWaterlooAPIFunction):
    path  = '/'
    service = "ExamSchedule"
    
@bind
class food_services_info(UWaterlooAPIFunction):
    path  = '/'
    service = "FoodServices"
    
@bind
class food_menu(UWaterlooAPIFunction):
    path  = '/'
    service = "FoodMenu"
    
@bind
class vending_machines_list(UWaterlooAPIFunction):
    path  = '/'
    service = "VendingMachines"
    
@bind
class watcard_vendors_list(UWaterlooAPIFunction):
    path  = '/'
    service = "WatcardVendors"

@bind
class professor_search(UWaterlooAPIFunction):
    """
    professor_search(q) where q is a string like "conrad"
    """
    path  = '/'
    service = "ProfessorSearch"
    arg_names = ["q"]
   
@bind
class professor_details(UWaterlooAPIFunction):
    """
    professor_details(q) where q a rate my professor id like "9845"
    """
    path  = '/'
    service = "ProfessorDetails"
    arg_names = ["q"] 

@bind
class programs_list(UWaterlooAPIFunction):
    path  = '/'
    service = "ProgramsList"

@bind
class recent_publications(UWaterlooAPIFunction):
    path  = '/'
    service = "RecentPublications"

@bind
class publication_details(UWaterlooAPIFunction):
    """
    publication_details(q) where q a publication ID "6030"
    """
    path  = '/'
    service = "PublicationDetails"
    arg_names = ["q"] 

@bind
class recent_dissertations(UWaterlooAPIFunction):
    path  = '/'
    service = "RecentDissertations"

@bind
class dissertations_details(UWaterlooAPIFunction):
    """
    publication_details(q) where q a dissertations ID "6030"
    """
    path  = '/'
    service = "DissertationDetails"
    arg_names = ["q"] 

@bind
class course_schedule(UWaterlooAPIFunction):
    """
    course_schedule(q, term=current_term) where q a publication ID "6030" and term is a term id like "1119".
    Term needs to be specified as a keyword argument
    """
    path  = '/'
    service = "Schedule"
    arg_names = ["q"] 

@bind
class weather(UWaterlooAPIFunction):
    path  = '/'
    service ="weather"

@bind
class staff_info(UWaterlooAPIFunction):
    """
    staff_info(q) where q a WATIAM username like "lwsmith"
    """
    path  = '/'
    service = "StaffInfo"
    arg_names = ["q"] 

@bind
class OMGUW(UWaterlooAPIFunction):
    path  = '/'
    service ="OMGUW"

@bind
class goose_watch(UWaterlooAPIFunction):
    path = '/'
    service = "GooseWatch"
