from evt_manager import EventManager
from django.shortcuts import render

emanager = EventManager()

def info(request, event_id):
    global emanager 
   
    current_event = emanager.get_event_by_id(event_id)
 
    context = {'current_event': current_event}
    return render(request, 'events/info.html', context)
    