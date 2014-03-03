# Just barely tests things to make sure they work

from uwaterlooapi import UWaterlooAPI; api = UWaterlooAPI(api_key='fda8e642f9c9480800e8c02896744288')

exclude = ['api_key', 'base_url']

for attr in dir(api):
    if attr.startswith("_"): continue
    if attr in exclude: continue
    f = getattr(api, attr)
    print attr
    try:
        f()
    except TypeError:
        f("query")
