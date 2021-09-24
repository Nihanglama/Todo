from re import U
from django.urls import path
from .views import TaskList,DetailList,Create,Update,Delete,Login,Register
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/',Register.as_view(),name='register'),
    path('user-login/',Login.as_view(),name='login'),
    path('user-logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('',TaskList.as_view(),name='list'),
    path('detail/<int:pk>/',DetailList.as_view(),name='detail'),
    path('create',Create.as_view(),name='create'),
    path('update/<int:pk>/',  Update.as_view(),name='update'),
    path('delete/<int:pk>/',Delete.as_view(),name='delete'),
]
