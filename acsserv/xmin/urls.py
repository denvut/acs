from django.conf.urls import url

from . import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin


urlpatterns = [
#    url(r'data/ChangeList.json$', ChangeList.as_view()),


    url(r'^$', StartXmin.as_view(), name='xmin-data'),
    url(r'^$', StartXmin.as_view(), name='xmin-index'),
]
