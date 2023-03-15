from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin, name='admin'),
    path('addapps/', views.addapps, name='addapps'),
    path('', views.user ),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('home/', views.home , name='home'),
    path('task/', views.task , name='task'),
    path('points/', views.points , name='points'),
    path('logout/', views.logout_view, name='logout'),
    
    path('my_view/<str:href_value>', views.openapp , name='my_view'),


]
