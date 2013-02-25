# -*- coding: utf8 -*-
#!/usr/bin/env python
'''
Created on Feb 22, 2013

@author: alekseynikiforov
'''

import time
import config
from mongoengine import *
from models import UserEvent

class EventManager(object):
    '''
    Event processing manager
    '''
    def __init__(self):
        '''
        Constructor
        '''
        connect(config.DB_NAME, host=config.DB_HOST, port=config.DB_PORT, username=config.DB_USER, password=config.DB_PASS)
    
    def register_event(self, uid, code, data):
        '''
        Save event
        '''
        user_event = UserEvent()
        user_event.code = code
        user_event.date = time.time()
        user_event.ext_data = data
        user_event.uid = uid      
        user_event.save()
        
        return {"result":"True"}
    
    def all_events(self):
        return list(UserEvent.objects())
    
    def get_event_by_id(self, event_id):
        try:
            return UserEvent.objects(id=event_id).first()
        except:
            return None
    