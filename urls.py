from django.conf.urls import patterns, url

from gif_or_jpeg import views 

urlpatterns = patterns('gif_or_jpeg.views',
	url(r'^$', 'index', name='index'),
	url(r'^question/$', 'question', name='new_question'),
	url(r'^question/(?P<session_id>\d+)/$', 'question', name='question'),
	url(r'^results/(?P<session_id>\d+)/$', 'results', name='results')
)
