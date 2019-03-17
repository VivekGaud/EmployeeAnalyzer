# Generated by Django 2.1.7 on 2019-02-27 13:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_employeelogininstances'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginInstances',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeUID', models.CharField(blank=True, max_length=150, null=True)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('user_instance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.EmployeeDetails')),
            ],
        ),
        migrations.DeleteModel(
            name='EmployeeLoginInstances',
        ),
    ]
