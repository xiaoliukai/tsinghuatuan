from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
                       url(r'^$', 'adminpage.views.home'),
                       url(r'^list/$', 'adminpage.views.activity_list'),
                       url(r'^detail/(?P<actid>\d+)/$', 'adminpage.views.activity_detail'),
                       url(r'^add/$', 'adminpage.views.activity_add'),
                       url(r'^modify/$', 'adminpage.views.activity_post'),
                       )