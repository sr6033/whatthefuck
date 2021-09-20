import json


class wtf(object):
    def __init__(self, **kwargs):
        data = json.dumps(kwargs)
        if kwargs:
            print('####################### [ FUCKED UP LOG ] #######################')
            print('## KWARGS: {}'.format(data))
        else:
            print('####################### [ FUCKED UP LOG ] #######################')
        import pdb;
        pdb.set_trace()

