from django.urls import path,include
from . import views

urlpatterns = [
    # path('', views.employee_form,name='employee_insert'), # get and post req. for insert operation
    path('', views.homepage,name='homepage'), # get and post req. for insert operation
    # path('<int:id>/', views.employee_form,name='employee_update'), # get and post req. for update operation
    # path('delete/<int:id>/',views.employee_delete,name='employee_delete'),
    path('list/',views.employee_list,name='employee_list'), # get req. to retrieve and display all records
    path("register/", views.register, name="register"),
    path("logout", views.logout_request, name="logout"),
    path("login", views.login_request, name="login"),
]