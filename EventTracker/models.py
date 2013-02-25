# -*- coding: utf8 -*-
#!/usr/bin/env python
'''
Created on Feb 22, 2013

@author: alekseynikiforov
'''

from mongoengine import Document, StringField, FloatField, DictField
from django.utils.datetime_safe import datetime

class Model(object):
    def __repr__(self):
        return str(self._id)
    ''' Define _id property which returns id of object as string '''
    def __id(self):
        if hasattr(self, "id"):
            return str(self.id)
        else:
            return ""
    _id = property(__id)

class UserEvent(Model, Document):
    meta = {'collection': 'stat.userevents'}
    uid              = StringField()
    date             = FloatField()
    code             = StringField()
    ext_data         = DictField() 
    
    @property
    def strdate(self):
        return datetime.utcfromtimestamp(self.date).strftime("%Y-%m-%d %H:%M:%S")

       
