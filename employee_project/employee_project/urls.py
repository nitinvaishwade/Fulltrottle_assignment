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
# router.register(r'users_test', views.GetActivityPeriod)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

# path('snippets/', views.SnippetList.as_view()),
    # path('snippets/<int:pk>/', views.SnippetDetail.as_view()),



urlpatterns = [
    path('admin/', admin.site.urls),
    path('users_test/', views.GetActivityPeriod.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('employee/',include('employee_register.urls'))
    # path('employee/',include('employee_register.urls'))
    url(r'^', include('employee_register.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
