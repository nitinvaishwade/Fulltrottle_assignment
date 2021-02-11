from .views import Index

from django.conf.urls import url






urlpatterns = [
    
    url(r'', Index, name='home'),



]