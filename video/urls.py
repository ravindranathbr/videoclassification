from django.conf.urls import include, url
from django.contrib import admin

from django.conf.urls import url

from . import views

app_name = 'video'
urlpatterns = [
    # ex: /polls/
    # url(r'^$', views.index, name='index'),
    # # ex: /polls/5/
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    
    # Alternative
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<video_id>[0-9]+)/download/$', views.download, name='download'),
    url(r'^(?P<video_id>[0-9]+)/predict/$', views.predict, name='predict'),
    url(r'^(?P<video_id>[0-9]+)/convert/$', views.convert_video_to_image, name='convert'),
    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # url(r'^(?P<video_id>[0-9]+)/vote/$', views.vote, name='video'),

    
]