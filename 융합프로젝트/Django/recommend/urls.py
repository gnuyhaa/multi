from django.urls import path
from . import views

app_name = 'recommend'

urlpatterns = [
    path('', views.index, name='index'),
    
    # path('', frige_list, name='frige_list'),
]