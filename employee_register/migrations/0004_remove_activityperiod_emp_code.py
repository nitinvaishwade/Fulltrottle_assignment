# Generated by Django 3.1.6 on 2021-02-14 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0003_activityperiod'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activityperiod',
            name='emp_code',
        ),
    ]
