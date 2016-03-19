from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', 'splash.views.index', name='index'),
]