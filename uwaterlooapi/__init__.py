__version__ = '0.3.0'

from shad import BaseAPI, APIFunction, get_bind


class UWaterlooAPI(BaseAPI):
    def __init__(self, api_key=None, base_url='http://api.uwaterloo.ca/v2/'):
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
    def get_path(self, kwargs):
        if 'output' in kwargs['params']:
            path = self.path + u'.' + kwargs['params']['output']
        else:
            path = self.path
        try:
            return path.format(*self.args)
        except IndexError:
            raise TypeError('Wrong number of arguments for url {}, {}'.format(path, self.args))


bind = get_bind(UWaterlooAPI)

# FoodServices

@bind
class menu(UWaterlooAPIFunction):
    path  = '/foodservices/menu'

@bind
class notes(UWaterlooAPIFunction):
    path  = '/foodservices/notes'

@bind
class diets(UWaterlooAPIFunction):
    path  = '/foodservices/diets'

@bind
class outlets(UWaterlooAPIFunction):
    path  = '/foodservices/outlets'

@bind
class locations(UWaterlooAPIFunction):
    path  = '/foodservices/locations'

@bind
class watcard(UWaterlooAPIFunction):
    path  = '/foodservices/watcard'

@bind
class announcements(UWaterlooAPIFunction):
    path  = '/foodservices/announcements'

@bind
class products(UWaterlooAPIFunction):
    path  = '/foodservices/products/{}'

@bind
class menu_by_week(UWaterlooAPIFunction):
    path = '/foodservices/{}/{}/menu'

@bind
class notes_by_week(UWaterlooAPIFunction):
    path = '/foodservices/{}/{}/notes'

@bind
class announcements_by_week(UWaterlooAPIFunction):
    path = '/foodservices/{}/{}/announcements'

# Courses

@bind
class courses(UWaterlooAPIFunction):
    path = '/courses'

@bind
class schedule_by_class_number(UWaterlooAPIFunction):
    path = '/courses/{}/schedule'

@bind
class course(UWaterlooAPIFunction):
    path = '/courses/{}/{}'

@bind
class course_schedule(UWaterlooAPIFunction):
    path = '/courses/{}/{}/schedule'

@bind
class course_prerequistes(UWaterlooAPIFunction):
    path = '/courses/{}/{}/prerequisites'

@bind
class course_examschedule(UWaterlooAPIFunction):
    path = '/courses/{}/{}/examschedule'
# Works needs to be done here...

# Events

@bind
class holidays(UWaterlooAPIFunction):
    path  = '/events/holidays'

# Weather

@bind
class current_weather(UWaterlooAPIFunction):
    path  = '/weather/current'

# Terms

@bind
class terms(UWaterlooAPIFunction):
    path = '/terms/list'

@bind
class term_examschedule(UWaterlooAPIFunction):
    path = '/terms/{}/examschedule'

@bind
class term_subject_schedule(UWaterlooAPIFunction):
    path = '/terms/{}/{}/schedule'

@bind
class term_course_schedule(UWaterlooAPIFunction):
    path = '/terms/{}/{}/{}/schedule'

@bind
class term_courses(UWaterlooAPIFunction):
    path = '/terms/{}/courses'

# Resources

@bind
class tutors(UWaterlooAPIFunction):
    path = '/resources/tutors'

@bind
class printers(UWaterlooAPIFunction):
    path = '/resources/printers'

@bind
class infosessions(UWaterlooAPIFunction):
    path = '/resources/infosessions'

# Definitions and Codes

@bind
class unit_codes(UWaterlooAPIFunction):
    path = '/codes/units'

@bind
class term_codes(UWaterlooAPIFunction):
    path = '/codes/terms'

@bind
class group_codes(UWaterlooAPIFunction):
    path = '/codes/groups'

@bind
class subject_codes(UWaterlooAPIFunction):
    path = '/codes/subjects'

@bind
class instruction_codes(UWaterlooAPIFunction):
    path = '/codes/instructions'

# Buildings

@bind
class building_list(UWaterlooAPIFunction):
    path = '/buildings/list'

@bind
class building(UWaterlooAPIFunction):
    path = '/buildings/{}'

@bind
class course_by_building_room(UWaterlooAPIFunction):
    path = '/buildings/{}/{}/courses'

# API

@bind
class api_usage(UWaterlooAPIFunction):
    path = '/api/usage'

@bind
class api_services(UWaterlooAPIFunction):
    path = '/api/services'

@bind
class api_methods(UWaterlooAPIFunction):
    path = '/api/methods'

@bind
class api_versions(UWaterlooAPIFunction):
    path = '/api/versions'

@bind
class api_changelog(UWaterlooAPIFunction):
    path = '/api/changelog'

# Server

@bind
class server_time(UWaterlooAPIFunction):
    path = '/server/time'

@bind
class server_codes(UWaterlooAPIFunction):
    path = '/server/codes'

