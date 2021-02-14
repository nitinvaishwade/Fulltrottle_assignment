from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib import admin
from django.conf.urls import url

from django.urls import include, path
from rest_framework import routers
from employee_register import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'users_active', views.ActivityPeriodViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('users_api/', views.GetActivityPeriod.as_view()),
    # path('accounts/', include('django.contrib.auth.urls')),
    url(r'^', include('employee_register.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
