

from django.contrib.auth.models import User
from rest_framework import serializers
from employee_register.models import ActivityPeriod


class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'email']

class ActivityPeriodSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    # user = serializers.SerializerMethodField('access_set')
    class Meta:
        model = ActivityPeriod
        fields = ['user', 'start_time', 'end_time']
    


    # def access_set(self, user):
    #     user_int = User.objects.get(username=user)
    #     queryset = ActivityPeriod.objects.filter(user_id=user_int)
    #     queryset = queryset | ActivityPeriod.objects.filter(user__username=user)
    #     queryset = queryset.distinct()
    #     serializer = UserSerializer(instance=queryset, many=True)
    #     return serializer.data