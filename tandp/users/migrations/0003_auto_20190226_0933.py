# Generated by Django 2.1.7 on 2019-02-26 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190226_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetails',
            name='password',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
