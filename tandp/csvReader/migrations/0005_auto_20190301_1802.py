# Generated by Django 2.1.7 on 2019-03-01 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csvReader', '0004_auto_20190301_1800'),
    ]

    operations = [
        migrations.RenameField(
            model_name='processcategory',
            old_name='description',
            new_name='all_included_process',
        ),
    ]
