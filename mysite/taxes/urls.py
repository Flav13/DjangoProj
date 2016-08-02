from django.conf.urls import url

from . import views
app_name = 'taxes'
urlpatterns = [
    url(r'^$',views.IndexView.as_view(), name='index'),
     url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^calculate/$',views.calculate, name='calculate'),
]
