from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf.urls import url, include
from django.contrib.auth.models import User

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'learning_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('learning_app.urls')),
)
