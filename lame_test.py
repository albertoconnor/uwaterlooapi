# Just barely tests things to make sure they work
import datetime

from uwaterlooapi import UWaterlooAPI; api = UWaterlooAPI(api_key='fda8e642f9c9480800e8c02896744288')

exclude = ['api_key', 'base_url']


dates = (datetime.datetime.now().year, datetime.datetime.now().date().isocalendar()[1])


args_map = {
    'announcements_by_week': dates,
    'menu_by_week': dates,
    'notes_by_week': dates,
    'course': ('CS', '486'),
    'course_examschedule': ('CS', '486'),
    'course_prerequistes': ('CS', '486'),
    'course_schedule': ('CS', '486'),
    'course_by_building_room': ('MC', '2038'),
    'term_course_schedule': ('1141', 'CS', '486'),
    'term_subject_schedule': ('1141', 'CS'),
}

for attr in dir(api):
    if attr.startswith("_"): continue
    if attr in exclude: continue
    f = getattr(api, attr)
    print(attr)
    try:
        f()
    except TypeError:
        try:
            args = ("query",)
            if attr in args_map:
                args = args_map[attr]
            f(*args)
        except Exception as e:
            print(e.message)
    except Exception as e:
        print(e.message)
