from django.conf.urls import patterns, url, include
from learning_app import views
from learning_project.settings import STATIC_ROOT, STATIC_URL
from django.conf.urls.static import static
from django.conf.urls import include

from rest_framework import routers
from learning_app.rest.rest_views import UserViewSet, GroupViewSet, LinkViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'links', LinkViewSet)


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^get_data$', views.get_data, name='get_data'),

    url(r'^rest-api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
) + static(STATIC_URL, document_root=STATIC_ROOT)