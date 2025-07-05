from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home,name='home'),
    path('predict/', views.predict, name='predict'),
    path('predictions/', views.all_predictions, name='all_predictions'),

]
