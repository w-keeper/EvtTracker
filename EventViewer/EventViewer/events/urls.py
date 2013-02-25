from django.conf.urls import patterns, url
from django.views.generic import ListView

from events import views
from evt_manager import EventManager

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
                queryset=EventManager().all_events(),
                context_object_name='events_list',
                template_name='events/index.html'),
            name='index'),
    url(r'^(?P<event_id>\w+)/$', 'events.views.info', name='info'),    
)