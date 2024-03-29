# Generated by Django 2.1.7 on 2019-02-26 03:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('emailUID', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=150, null=True)),
                ('password', models.CharField(max_length=150, null=True)),
                ('password_open', models.CharField(max_length=150, null=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
            ],
        ),
    ]
