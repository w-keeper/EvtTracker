# -*- coding: utf8 -*-
#!/usr/bin/env python
'''
Created on Feb 22, 2013

@author: alekseynikiforov
'''

import json
import config
from flask import Flask
from flask import request

from evt_manager import EventManager

app = Flask(__name__)

# API methods

event_manager = EventManager()

@app.route("/event/register", methods=['POST'])
def register_event():
    global event_manager
    req = request.json
    return json.dumps(event_manager.register_event(req["uid"], req["code"], req["data"]), separators=(',',':')) 

if __name__ == "__main__":
    app.run(debug=True, host=config.SERVICE_HOST, port=config.SERVICE_PORT)