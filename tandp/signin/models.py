from django.db import models

class employee_data(models.Model):
	employee_ID = models.AutoField(primary_key=True)
	employee_name = models.CharField(max_length = 150)
	