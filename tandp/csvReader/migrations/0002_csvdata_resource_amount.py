# Generated by Django 2.1.7 on 2019-02-20 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvReader', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='csvdata',
            name='resource_amount',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
