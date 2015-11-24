from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import login, logout
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^login/$',  login),
                       url(r'^accounts/logout/$', logout),
                       url(r'^home/','system.views.Home',name="Home"),
                       url(r'^timetable/','system.views.Timetable',name="Timetable"),
                       url(r'^result/','system.views.Result',name="Result"),
                       url(r'^compulsory/','system.views.Compulsory',name="Compulsory"),
                       url(r'^socialism/','system.views.Socialism',name="Socialism"),
                       url(r'^arbitrary/','system.views.Arbitrary',name="Aarbitrary"),
                       url(r'^management/','system.views.Management',name="Introduction"),
                       url(r'^room1/','system.views.Room1',name="Room1"),
                       url(r'^score/','system.views.Score',name="Socre"),
                       url(r'^medias/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT },name="media"),
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^project/', include('project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
