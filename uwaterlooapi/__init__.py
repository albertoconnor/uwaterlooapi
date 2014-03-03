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
            return self.path + u'.' + kwargs['params']['output']
        return self.path

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

# Course

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


