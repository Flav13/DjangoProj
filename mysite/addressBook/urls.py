from django.conf.urls import patterns, url

from rest_framework.urlpatterns import format_suffix_patterns

from addressBook import views

app_name = 'addressBook'
urlpatterns = [
    url(r'^$', views.index_view, name='index_view'),
    url(r'^contacts/$', views.ContactsView.as_view(), name='contact-list'),
    url(r'',views.ContactInstanceView.as_view(), name='contact-instance'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
