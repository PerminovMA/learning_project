from django.conf.urls import patterns, url
from learning_app import views
from learning_project.settings import STATIC_ROOT, STATIC_URL
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^get_data$', views.get_data, name='get_data'),
) + static(STATIC_URL, document_root=STATIC_ROOT)