from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),        
    path('test', views.test),
    path('gu',views.gu),
    path('signup', views.signup),
    path('git', views.git)
    
    
 ]
