from django.db import models
import random
import datetime
import hashlib


class EmployeeDetails(models.Model):
	name = models.CharField(max_length = 100,blank = True, null = True)
	emailUID = models.CharField(max_length = 200,blank = True, null = True)
	email = models.CharField(max_length = 150,blank = True, null = True)
	password = models.CharField(max_length = 150,blank = True, null = True)
	password_open = models.CharField(max_length = 150, null = True)
	is_admin = models.BooleanField(default = False)
	is_deleted = models.BooleanField(default = False)
	created_at = models.DateTimeField(null = True, blank = True, default = datetime.datetime.now)
	def __str__(self):
		return str(self.email)
	def save(self, *args, **kwargs):
		self.password = hashlib.md5(self.password_open.encode()).hexdigest()
		super(EmployeeDetails, self).save(*args, **kwargs)



class EmployeeRegister(models.Model):
	name = models.CharField(max_length = 100,blank = True, null = True)
	emailUID = models.CharField(max_length = 200,blank = True, null = True)
	email = models.CharField(max_length = 150,blank = True, null = True)
	password = models.CharField(max_length = 150,blank = True, null = True)
	password_open = models.CharField(max_length = 150, null = True)
	is_admin = models.BooleanField(default = False)
	is_deleted = models.BooleanField(default = False)
	created_at = models.DateTimeField(null = True, blank = True, default = datetime.datetime.now)

	def save(self, *args, **kwargs):
		self.password = hashlib.md5(self.password_open.encode()).hexdigest()
		super(EmployeeRegister, self).save(*args, **kwargs)


class LoginInstances(models.Model):
	user_instance = models.ForeignKey(EmployeeDetails,blank = True, null = True, on_delete=models.CASCADE)
	employeeUID = models.CharField(max_length = 150,blank = True, null = True)
	created_at = models.DateTimeField(null = True, blank = True, default = datetime.datetime.now)
	difference_reason = models.CharField(max_length = 150,blank = True, null = True)
	target_achieved = models.BooleanField(default = False)
	is_deleted = models.BooleanField(default = False)

	def __str__(self):
		return str(self.created_at)




