from django.conf.urls import include, url
from . import views

urlpatterns = [
    #url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.login, name='login'),
    url(r'^account_created/$', views.account_created, name='account_created'),
    url(r'^create/$',views.create_account, name='create_account'),
    url(r'^create/details/(?P<pk>[0-9]+)/$',views.details, name='details'),
    url(r'^preference/(?P<pk>[0-9]+)/$',views.preference, name ='preference')
    #url(r'^post/new/(?P<pk>[0-9]+)/$', views.post_new, name='post_new'),

]