from django.urls import include, path
from django.conf.urls import handler404

from . import views


app_name='job'

handler404='jobs.views.view_404'



urlpatterns = [
    path('',views.home , name='home'),
    path('detail/<slug>',views.detail , name='detail'),
]