from django.urls import include, path
from . import views


app_name='blog'




urlpatterns = [
    path('',views.blog , name='bloghome'),
    path('<slug>/',views.single , name='single'),
    path('like/<slug>',views.like_unlike , name='like'),
]