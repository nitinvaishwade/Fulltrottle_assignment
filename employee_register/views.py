import random 

from faker import Faker
import dumper
from random import randint
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Employee
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, ActivityPeriodSerializer
from django.contrib import messages
from employee_register.models import ActivityPeriod
from datetime import datetime, timedelta
import logging
from django.http import JsonResponse
from rest_framework import mixins
from rest_framework import generics



import logging, logging.config
import sys

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO'
    }
}

logging.config.dictConfig(LOGGING)



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ActivityPeriodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ActivityPeriod.objects.all()
    serializer_class = ActivityPeriodSerializer
    permission_classes = [permissions.IsAuthenticated]

import requests

# @login_required
def homepage(request):
    """
    Home page
    """
    if request.method == 'POST':
        logging.info('given_number')
        GenerateFakeData()
        return redirect('/list')
        
    if request.method == 'GET':
        given_input = request.GET.get('show_answer')
        if given_input:

            # response = requests.get("http://127.0.0.1:8000/users_api/")
            return redirect('/users_api')

    return render(request, "homepage.html")

# @login_required
def employee_list(request):
    context = {'employee_list': ActivityPeriod.objects.all()}
    return render(request, "employee_register/employee_list.html", context)

# @login_required
# def employee_form(request, id=0):
#     if request.method == "GET":
#         if id == 0:
#             form = EmployeeForm()
#         else:
#             employee = Employee.objects.get(pk=id)
#             form = EmployeeForm(instance=employee)
#         return render(request, "employee_register/employee_form.html", {'form': form})
#     else:
#         if id == 0:
#             form = EmployeeForm(request.POST)
#         else:
#             employee = Employee.objects.get(pk=id)
#             form = EmployeeForm(request.POST,instance= employee)
#         if form.is_valid():
#             form.save()
#         return redirect('/list')

# @login_required
# def employee_delete(request,id):
#     employee = Employee.objects.get(pk=id)
#     employee.delete()
#     return redirect('/list')


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")





def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "You are now logged in")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = LoginForm()
    return render(request = request,
                    template_name = "registration/login.html",
                    context={"form":form})



def register(request):
    logging.info("aaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    if request.method == 'POST':
        logging.info("inside posr=============")
        form = UserCreationForm(request.POST)
        logging.info(form)
        if form.is_valid():
            form.save()
            logging.info('inside valid')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            # login(request, user)
            logging.info("after login============")
            logging.info("before registre==========")
            if user is not None:
                login(request, user)
                messages.info(request, "You are now logged in")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
            # return redirect('/')
        else:
            messages.error(request, "Invalid password.")
            form = UserCreationForm()

    else:
        form = UserCreationForm()
    return render(request = request,
            template_name = "registration/register.html",
            context={"form":form})




    # form = RegisterForm()
    



def GenerateFakeData():
    for i in range(5):
        faker = Faker()
        user_mail = faker.email()
        first_name = faker.first_name()
        last_name = faker.last_name()
        username = "{}{}".format(first_name, last_name)
        user = User.objects.create_user(username, user_mail, 'edx')
        user.save()
        count = 0
        for user_time in range(2):
            now = datetime.now()
            n_number = random.randint(2,9)
            end_time = datetime.now() + timedelta(hours=n_number)
            if count > 0:
                now = datetime.now() + timedelta(days=5)
                end_time = now + timedelta(hours=n_number)

            ActivityPeriod.objects.create(user = user, start_time=now, end_time=end_time)
            count = 1




class GetActivityPeriod(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = ActivityPeriod.objects.all()
    serializer_class = ActivityPeriodSerializer

    def get(self, request, *args, **kwargs):
        all_data = ActivityPeriod.objects.all()
        all_user_records = {}
        members =[]
        all_user_records_add = {}
        activity_periods =[]
        
        user_list = []
        for row in all_data:
            if row.user.username in user_list:
                start_end_time = {'start_time': row.start_time, 'end_time':row.end_time}
                add_time_periods = []
                for member_row in members:
                    if member_row['real_name'] == row.user.username:
                        add_time_periods.extend(member_row['activity_periods'])
                        add_time_periods.append(start_end_time)
                        logging.info(add_time_periods)
                        member_row['activity_periods'] = add_time_periods 
            else:
                user_list.append(row.user.username)
                start_end_time = {'start_time': row.start_time, 'end_time':row.end_time}
                all_user_records_add['real_name'] = row.user.username
                all_user_records_add['activity_periods'] = [start_end_time]
                members.append(all_user_records_add)
                all_user_records_add={}
        all_user_records['members'] = members
        return JsonResponse(all_user_records, safe=False)