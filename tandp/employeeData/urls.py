from django.conf.urls import url
from .import views
from django.conf.urls import url,include

urlpatterns = [ 
	url(r'^$',views.process_data, name = 'process_data'),
]