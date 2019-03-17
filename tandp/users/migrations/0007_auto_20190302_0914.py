# Generated by Django 2.1.7 on 2019-03-02 03:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190227_1853'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('emailUID', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=150, null=True)),
                ('password', models.CharField(blank=True, max_length=150, null=True)),
                ('password_open', models.CharField(max_length=150, null=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='logininstances',
            name='difference_reason',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='logininstances',
            name='target_achieved',
            field=models.BooleanField(default=False),
        ),
    ]