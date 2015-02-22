from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'learning_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('learning_app.urls')),
    url(r'^index/', include('learning_app.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
