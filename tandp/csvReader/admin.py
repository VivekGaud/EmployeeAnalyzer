from django.contrib import admin
from csvReader.models import *

admin.site.register(ProcessCategory)
admin.site.register(ProcessDetails)
admin.site.register(CsvData)
admin.site.register(CategoryDataPerDay)

