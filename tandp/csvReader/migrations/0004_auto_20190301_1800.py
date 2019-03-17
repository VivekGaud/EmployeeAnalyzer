# Generated by Django 2.1.7 on 2019-03-01 12:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('csvReader', '0003_auto_20190222_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryDataPerDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ReadTransferCount', models.CharField(blank=True, max_length=150, null=True)),
                ('WriteTransferCount', models.CharField(blank=True, max_length=150, null=True)),
                ('KernelModeTime', models.CharField(blank=True, max_length=150, null=True)),
                ('WorkingSetSize', models.CharField(blank=True, max_length=150, null=True)),
                ('UserModeTime', models.CharField(blank=True, max_length=150, null=True)),
                ('ThreadCount', models.CharField(blank=True, max_length=150, null=True)),
                ('QuotaPeakPagedPoolUsage', models.CharField(blank=True, max_length=150, null=True)),
                ('Priority', models.CharField(blank=True, max_length=150, null=True)),
                ('PeakWorkingSetSize', models.CharField(blank=True, max_length=150, null=True)),
                ('PeakPageFileUsage', models.CharField(blank=True, max_length=150, null=True)),
                ('employeeUID', models.CharField(blank=True, max_length=150, null=True)),
                ('CreationDate', models.CharField(blank=True, max_length=150, null=True)),
                ('created_at', models.CharField(blank=True, max_length=150, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('process_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='csvReader.ProcessCategory')),
            ],
        ),
        migrations.RemoveField(
            model_name='csvdata',
            name='processName',
        ),
        migrations.RemoveField(
            model_name='csvdata',
            name='resource_amount',
        ),
        migrations.AddField(
            model_name='csvdata',
            name='CreationDate',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='csvdata',
            name='Description',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='csvdata',
            name='KernelModeTime',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='csvdata',
            name='Name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='csvdata',
            name='ParentProcessId',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='csvdata',
            name='PeakPageFileUsage',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='csvdata',
            name='PeakWorkingSetSize',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='csvdata',
            name='Priority',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='csvdata',
            name='QuotaPeakPagedPoolUsage',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='csvdata',
            name='ReadTransferCount',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='csvdata',
            name='ThreadCount',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='csvdata',
            name='UserModeTime',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='csvdata',
            name='WorkingSetSize',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='csvdata',
            name='WriteTransferCount',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='csvdata',
            name='created_at',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='csvdata',
            name='employeeUID',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='csvdata',
            name='process_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='csvReader.ProcessCategory'),
        ),
        migrations.AddField(
            model_name='csvdata',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='csvdata',
            name='processId',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
