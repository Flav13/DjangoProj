from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from booking import views

app_name = 'booking'
urlpatterns = [
    url(r'^$', views.index_view, name='index_view'),
    url(r'^create_user/$', views.createUser, name='userCreation'),
    url(r'^user/$', views.UserView.as_view(), name='user-list'),
    url(r'^create_booking/$', views.userAuthView, name='bookingCreation'),
    url(r'^create_booking/auth/bookings', views.BookingView.as_view(), name='booking-list'),
    url(r'^create_booking/auth$', views.authenticateUser, name='authenticateUser'),
     url(r'^create_booking/auth/bookings/(?P<pk>[\d]+)$', views.BookingInstanceView.as_view(), name='bookingSuccess'),
     url(r'^user/(?P<pk>[\d]+)$', views.UserInstanceView.as_view(), name='user-instance'),
    ]
