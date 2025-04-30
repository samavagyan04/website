from django.urls import path
from .views import *

handler404 = 'main.views.page404'

urlpatterns=[
    path('',HomePage,name='home'),
]