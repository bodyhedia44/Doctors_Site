from django.urls import include, path
from . import views


app_name='accounts'




urlpatterns = [
    path('edit/<slug>',views.edit_prof , name='edit_prof'),
    path('profile/',views.profile , name='profile'),
    path('signup/',views.signup , name='signup'),
    path('editprofile/',views.ed , name='ed'),

]