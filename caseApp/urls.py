from django.conf.urls import include,  url
from django.contrib import admin
from . import views
from caseApp.views import publishCase

urlpatterns = [
    url(r'^admin/',  (admin.site.urls)),
    
   url(r'^publishCase/$', publishCase),
   url(r'^$',  views.publishCase, name='publishCase'),
]

#''' url(r'', include('caseApp.urls')),'''