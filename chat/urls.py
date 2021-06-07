from django.urls import path
from . import views
from chat.views import upload_video,display,cam,cam2

from django.conf.urls.static import static
from django.conf import  settings
 

app_name = 'home'

urlpatterns = [
	# path('call', views.call, name='call'),
	# path('video6', views.video6, name='video6'),
	# path('video5', views.video5, name='video5'),
	# path('video3', views.video3, name='video3'),
	# path('video', views.video, name='video'),
	path('', views.home, name='index'),
    path('upload/',upload_video,name='upload'),
    path('videos/',display,name='videos'),
	path('cam/',cam,name='cam'),
	path('cam2/',cam2,name='cam2'),
]