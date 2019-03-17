from django.db import models
import datetime


class ProcessCategory(models.Model):
	name = models.CharField(max_length = 100, null = True)
	# description = models.CharField(max_length = 500, null = True)
	all_included_process = models.CharField(max_length = 500, null = True)
	is_deleted = models.BooleanField(default = False)

	def __str__(self):
		return str(self.name)

class ProcessDetails(models.Model):
	process_category = models.ForeignKey(ProcessCategory,blank = True, null = True, on_delete=models.CASCADE)
	process_name = models.CharField(max_length = 100, blank = True, null = True) 
	is_deleted = models.BooleanField(default = False) 
	def __str__(self):
		return str(self.process_name)

class CategoryDataPerDay(models.Model):
	process_category = models.ForeignKey(ProcessCategory,blank = True, null = True, on_delete=models.CASCADE)
	ReadTransferCount = models.CharField(max_length = 150, blank = True, null = True)
	WriteTransferCount = models.CharField(max_length = 150, blank = True, null = True)
	KernelModeTime = models.CharField(max_length = 150, blank = True, null = True)
	WorkingSetSize = models.CharField(max_length = 150, blank = True, null = True)
	UserModeTime = models.CharField(max_length = 150, blank = True, null = True)
	ThreadCount = models.CharField(max_length = 150, blank = True, null = True)
	QuotaPeakPagedPoolUsage = models.CharField(max_length = 150, blank = True, null = True)
	Priority = models.CharField(max_length = 150, blank = True, null = True)
	PeakWorkingSetSize = models.CharField(max_length = 150, blank = True, null = True)
	PeakPageFileUsage = models.CharField(max_length = 150, blank = True, null = True)
	employeeUID = models.CharField(max_length = 150, blank = True, null = True)
	CreationDate = models.CharField(max_length = 150, blank = True, null = True)
	created_at = models.CharField(max_length = 150, blank = True, null = True)

	is_deleted = models.BooleanField(default = False)
	def __str__(self):
		return str(self.process_category)

class CsvData(models.Model):
	process_category = models.ForeignKey(ProcessCategory,blank = True, null = True, on_delete=models.CASCADE)
	process_key = models.ForeignKey(ProcessDetails,blank = True, null = True, on_delete=models.CASCADE)
	Name = models.CharField(max_length = 150, blank = True, null = True)
	Description = models.CharField(max_length = 150, blank = True, null = True)
	CreationDate = models.CharField(max_length = 150, blank = True, null = True)
	created_at = models.CharField(max_length = 150, blank = True, null = True)
	ParentProcessId = models.CharField(max_length = 150, blank = True, null = True)
	ReadTransferCount = models.CharField(max_length = 150, blank = True, null = True)
	WriteTransferCount = models.CharField(max_length = 150, blank = True, null = True)
	KernelModeTime = models.CharField(max_length = 150, blank = True, null = True)
	WorkingSetSize = models.CharField(max_length = 150, blank = True, null = True)
	UserModeTime = models.CharField(max_length = 150, blank = True, null = True)
	ThreadCount = models.CharField(max_length = 150, blank = True, null = True)
	QuotaPeakPagedPoolUsage = models.CharField(max_length = 150, blank = True, null = True)
	Priority = models.CharField(max_length = 150, blank = True, null = True)
	PeakWorkingSetSize = models.CharField(max_length = 150, blank = True, null = True)
	PeakPageFileUsage = models.CharField(max_length = 150, blank = True, null = True)
	employeeUID = models.CharField(max_length = 150, blank = True, null = True)
	processId = models.CharField(max_length = 100, blank = True, null = True)

	updated_at = models.DateTimeField(null = True, blank = True, default = datetime.datetime.now)
	is_deleted = models.BooleanField(default = False)
	def __str__(self):
		return str(self.Name)
