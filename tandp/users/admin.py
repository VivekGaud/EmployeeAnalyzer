from django.contrib import admin
from .models import *
from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin



class EmployeeDetailsAdmin(SuperModelAdmin):
	model = EmployeeDetails

admin.site.register(EmployeeDetails,EmployeeDetailsAdmin)
admin.site.register(LoginInstances)
