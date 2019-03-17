import pyrebase 
import threading, calendar
from tandp.settings import FCMCONFIG
from csvReader.models import *
import csv, time, wmi, pythoncom
from django.utils import timezone
from datetime import datetime

def init_fcm_auth():
	firebase = pyrebase.initialize_app(FCMCONFIG)
	auth = firebase.auth()
	return firebase,auth

def get_fcm_token(em_id="iamvickypedia@root.com", passw="iamvickypedia"):
	firebase = pyrebase.initialize_app(FCMCONFIG)

	auth = firebase.auth()
	user = auth.sign_in_with_email_and_password(em_id, passw)
	# user = auth.refresh(user['refreshToken'])
	id_token = user["localId"]
	# import pdb; pdb.set_trace()

	return firebase,id_token

# class TaskThread(threading.Thread):
# 	"""Thread that executes a task every N seconds"""
	
# 	def __init__(self):
# 		threading.Thread.__init__(self)
# 		self._finished = threading.Event()
# 		self._interval = 15.0
	
# 	def setInterval(self, interval):
# 		"""Set the number of seconds we sleep between executing our task"""
# 		self._interval = interval
	
# 	def shutdown(self):
# 		"""Stop this thread"""
# 		self._finished.set()
	
# 	def run(self):
# 		while 1:
# 			if self._finished.isSet(): return
# 			self.task()
# 			# sleep for interval or until shutdown
# 			self._finished.wait(self._interval)
	
# 	def task(self):
# 		"""The task done by this thread - override in subclasses"""
# 		print("running")
# 		time.sleep(5)

# 		return True

# from schedule import Scheduler

# def run_continuously(self, interval=1):

#     cease_continuous_run = threading.Event()

#     class ScheduleThread(threading.Thread):

#         @classmethod
#         def run(cls):
#             while not cease_continuous_run.is_set():
#                 self.run_pending()
#                 time.sleep(interval)

#     continuous_thread = ScheduleThread()
#     continuous_thread.setDaemon(True)
#     continuous_thread.start()
#     return cease_continuous_run


# Scheduler.run_continuously = run_continuously
# add func to add unique process with category

def process_gathering(request):
	# import pdb; pdb.set_trace()
	pythoncom.CoInitialize()
	c = wmi.WMI()
	proc = c.Win32_Process ()
	firebase_array = []
	for process in proc:
		try:
		    pro_category = ProcessCategory.objects.get(all_included_process__icontains = process.Name)
		except ProcessCategory.DoesNotExist:
		    pro_category = ProcessCategory.objects.get(name="Others")
		else:
			pass

		if ProcessDetails.objects.filter(process_name = process.Name, is_deleted = False).exists():
			process_detail = ProcessDetails.objects.get(process_name = process.Name, is_deleted = False)
		else:
			process_detail = ProcessDetails.objects.create(process_name = process.Name,process_category = pro_category, is_deleted = False)
		
		
		# process_image = {
		# 	"ReadTransferCount": process.ReadTransferCount,
		# 	"Name": process.Name,
		# 	"WriteTransferCount": process.WriteTransferCount,
		# 	"CreationDate": process.CreationDate,
		# 	"Description": process.Description,
		# 	"KernelModeTime": process.KernelModeTime,
		# 	"WorkingSetSize": process.WorkingSetSize,
		# 	"UserModeTime": process.UserModeTime,
		# 	"ThreadCount": process.ThreadCount,
		# 	"QuotaPeakPagedPoolUsage": process.QuotaPeakPagedPoolUsage,
		# 	"Priority": process.Priority,
		# 	"PeakWorkingSetSize": process.PeakWorkingSetSize,
		# 	"PeakPageFileUsage": process.PeakPageFileUsage,
		# 	"ParentProcessId": process.ParentProcessId,
		# 	"created_at":timezone.now().timezone(),
		# 	"category_id" : pro_category.pk,
		# 	"employeeUID": request.session.token
		# }

		# if CsvData.objects.filter(employeeUID= process.employeeUID,Name= process.Name,processId= process.processId).exists():
		# 	csvdata = CsvData.objects.get(employeeUID= process.employeeUID,Name= process.Name,processId= process.processId)
		# 	csvdata.ReadTransferCount = process.ReadTransferCount 
		# 	csvdata.WriteTransferCount = process.WriteTransferCount 
		# 	csvdata.KernelModeTime = process.KernelModeTime 
		# 	csvdata.WorkingSetSize = process.WorkingSetSize 
		# 	csvdata.UserModeTime = process.UserModeTime 
		# 	csvdata.ThreadCount = process.ThreadCount 
		# 	csvdata.QuotaPeakPagedPoolUsage = process.QuotaPeakPagedPoolUsage 
		# 	csvdata.Priority = process.Priority 
		# 	csvdata.PeakWorkingSetSize = process.PeakWorkingSetSize 
		# 	csvdata.PeakPageFileUsage = process.PeakPageFileUsage 
		# 	csvdata.process_key = process.process_detail
		# 	csvdata.process_category = pro_category
				
		if CsvData.objects.filter(employeeUID= request.session["token"],Name= process.Name, processId= process.processId,process_category = pro_category,process_key = process_detail).exists():
			# csvdata = CsvData.objects.get(employeeUID= process.employeeUID,Name= process.Name,processId= process.processId)
			csvdata = CsvData.objects.get(employeeUID= request.session["token"],Name= process.Name,processId= process.processId,process_category = pro_category,process_key = process_detail)
			csvdata.ReadTransferCount = int(csvdata.ReadTransferCount or 0) + (int(csvdata.ReadTransferCount or 0) - int(process.ReadTransferCount)) 
			csvdata.WriteTransferCount = int(csvdata.WriteTransferCount or 0) + (int(csvdata.WriteTransferCount or 0) - int(process.WriteTransferCount)) 
			csvdata.KernelModeTime = int(csvdata.KernelModeTime or 0) + (int(csvdata.KernelModeTime or 0) - int(process.KernelModeTime)) 
			csvdata.WorkingSetSize = int(csvdata.WorkingSetSize or 0) + (int(csvdata.WorkingSetSize or 0) - int(process.WorkingSetSize)) 
			csvdata.UserModeTime = int(csvdata.UserModeTime or 0) + (int(csvdata.UserModeTime or 0) - int(process.UserModeTime)) 
			csvdata.ThreadCount = int(csvdata.ThreadCount or 0) + (int(csvdata.ThreadCount or 0) - int(process.ThreadCount)) 
			csvdata.QuotaPeakPagedPoolUsage = int(csvdata.QuotaPeakPagedPoolUsage or 0) + (int(csvdata.QuotaPeakPagedPoolUsage or 0) - int(process.QuotaPeakPagedPoolUsage)) 
			csvdata.Priority = int(csvdata.Priority or 0) + (int(csvdata.Priority or 0) - int(process.Priority)) 
			csvdata.PeakWorkingSetSize = int(csvdata.PeakWorkingSetSize or 0) + (int(csvdata.PeakWorkingSetSize or 0) - int(process.PeakWorkingSetSize)) 
			csvdata.PeakPageFileUsage = int(csvdata.PeakPageFileUsage or 0) + (int(csvdata.PeakPageFileUsage or 0) - int(process.PeakPageFileUsage)) 
			csvdata.created_at = timezone.now().timestamp()
		else:
			csvdata = CsvData.objects.create(employeeUID= request.session["token"],Name= process.Name,processId= process.processId,process_category = pro_category,process_key = process_detail)
			csvdata.ReadTransferCount = int(process.ReadTransferCount)
			csvdata.WriteTransferCount = int(process.WriteTransferCount)
			csvdata.KernelModeTime = int(process.KernelModeTime)
			csvdata.WorkingSetSize = int(process.WorkingSetSize)
			csvdata.UserModeTime = int(process.UserModeTime)
			csvdata.ThreadCount = int(process.ThreadCount)
			csvdata.QuotaPeakPagedPoolUsage = int(process.QuotaPeakPagedPoolUsage)
			csvdata.Priority = int(process.Priority)
			csvdata.PeakWorkingSetSize = int(process.PeakWorkingSetSize)
			csvdata.PeakPageFileUsage = int(process.PeakPageFileUsage)
			csvdata.created_at = timezone.now().timestamp()
		csvdata.save()

		# created_at = time.mktime(timezone.now().date().timetuple()) #timestamp of the date

		created_at = timezone.now().date() #timestamp of the date

		if not datetime.fromtimestamp(float(csvdata.created_at)).date() == created_at:
			category_data = CategoryDataPerDay(process_category = pro_category,employeeUID = request.session["token"], created_at = calendar.timegm(timezone.now().date().timetuple()) )
			category_data.ReadTransferCount = int(csvdata.ReadTransferCount)
			category_data.WriteTransferCount = int(csvdata.WriteTransferCount)
			category_data.KernelModeTime = int(csvdata.KernelModeTime)
			category_data.WorkingSetSize = int(csvdata.WorkingSetSize)
			category_data.UserModeTime = int(csvdata.UserModeTime)
			category_data.ThreadCount = int(csvdata.ThreadCount)
			category_data.QuotaPeakPagedPoolUsage = int(csvdata.QuotaPeakPagedPoolUsage)
			category_data.Priority = int(csvdata.Priority)
			category_data.PeakWorkingSetSize = int(csvdata.PeakWorkingSetSize)
			category_data.PeakPageFileUsage = int(csvdata.PeakPageFileUsage)
			category_data.save()
		else:
			if CategoryDataPerDay.objects.filter(process_category = pro_category, employeeUID = request.session["token"] ,created_at=calendar.timegm(timezone.now().date().timetuple())).exists():
				category_data = CategoryDataPerDay.objects.get(process_category = pro_category, created_at = calendar.timegm(timezone.now().date().timetuple()) )
				category_data = CategoryDataPerDay.objects.filter(process_category = pro_category, created_at = calendar.timegm(timezone.now().date().timetuple()) ).order_by("-pk")[0]
				category_data.ReadTransferCount = int(category_data.ReadTransferCount or 0) + (int(category_data.ReadTransferCount or 0)  - int(csvdata.ReadTransferCount))
				category_data.WriteTransferCount = int(category_data.WriteTransferCount or 0 ) +(int(category_data.WriteTransferCount or 0 ) -  int(csvdata.WriteTransferCount))
				category_data.KernelModeTime = int(category_data.KernelModeTime or 0 ) +(int(category_data.KernelModeTime or 0 ) -  int(csvdata.KernelModeTime))
				category_data.WorkingSetSize = int(category_data.WorkingSetSize or 0 ) +(int(category_data.WorkingSetSize or 0 ) -  int(csvdata.WorkingSetSize))
				category_data.UserModeTime = int(category_data.UserModeTime or 0 ) +(int(category_data.UserModeTime or 0 ) -  int(csvdata.UserModeTime))
				category_data.ThreadCount = int(category_data.ThreadCount or 0 ) +(int(category_data.ThreadCount or 0 ) -  int(csvdata.ThreadCount))
				category_data.QuotaPeakPagedPoolUsage = int(category_data.QuotaPeakPagedPoolUsage or 0 ) +(int(category_data.QuotaPeakPagedPoolUsage or 0 ) -  int(csvdata.QuotaPeakPagedPoolUsage))
				category_data.Priority = int(category_data.Priority or 0 ) +(int(category_data.Priority or 0 ) -  int(csvdata.Priority))
				category_data.PeakWorkingSetSize = int(category_data.PeakWorkingSetSize or 0 ) +(int(category_data.PeakWorkingSetSize or 0 ) -  int(csvdata.PeakWorkingSetSize))
				category_data.PeakPageFileUsage = int(category_data.PeakPageFileUsage or 0 ) +(int(category_data.PeakPageFileUsage or 0 ) -  int(csvdata.PeakPageFileUsage))
				category_data.save()
			else:
				category_data = CategoryDataPerDay(process_category = pro_category,employeeUID = request.session["token"], created_at = calendar.timegm(timezone.now().date().timetuple()) )
				category_data.ReadTransferCount = int(csvdata.ReadTransferCount)
				category_data.WriteTransferCount = int(csvdata.WriteTransferCount)
				category_data.KernelModeTime = int(csvdata.KernelModeTime)
				category_data.WorkingSetSize = int(csvdata.WorkingSetSize)
				category_data.UserModeTime = int(csvdata.UserModeTime)
				category_data.ThreadCount = int(csvdata.ThreadCount)
				category_data.QuotaPeakPagedPoolUsage = int(csvdata.QuotaPeakPagedPoolUsage)
				category_data.Priority = int(csvdata.Priority)
				category_data.PeakWorkingSetSize = int(csvdata.PeakWorkingSetSize)
				category_data.PeakPageFileUsage = int(csvdata.PeakPageFileUsage)
				category_data.created_at = calendar.timegm(timezone.now().date().timetuple())
				category_data.save()

			# this will give the one time executed process details. We want a consolidated details fr all process/Category
			# according to a login session
		# firebase_array.append(process_image)

	return firebase_array

def add_or_edit_csvcategory_data(csv_arr_src,csv_arr_dst,mode):
	if mode == "add":
		csv_arr_dst.ReadTransferCount = int(csv_arr_src["ReadTransferCount"])
		csv_arr_dst.WriteTransferCount = int(csv_arr_src["WriteTransferCount"])
		csv_arr_dst.KernelModeTime = int(csv_arr_src["KernelModeTime"])
		csv_arr_dst.WorkingSetSize = int(csv_arr_src["WorkingSetSize"])
		csv_arr_dst.UserModeTime = int(csv_arr_src["UserModeTime"])
		csv_arr_dst.ThreadCount = int(csv_arr_src["ThreadCount"])
		csv_arr_dst.QuotaPeakPagedPoolUsage = int(csv_arr_src["QuotaPeakPagedPoolUsage"])
		csv_arr_dst.Priority = int(csv_arr_src["Priority"])
		csv_arr_dst.PeakWorkingSetSize = int(csv_arr_src["PeakWorkingSetSize"])
		csv_arr_dst.PeakPageFileUsage = int(csv_arr_src["PeakPageFileUsage"])
	elif mode == "update":
		csv_arr_dst.ReadTransferCount = int(csv_arr_dst.ReadTransferCount or 0) + (int(csv_arr_dst.ReadTransferCount or 0) - int(csv_arr_src["ReadTransferCount"]))
		csv_arr_dst.WriteTransferCount = int(csv_arr_dst.WriteTransferCount or 0) + (int(csv_arr_dst.WriteTransferCount or 0) - int(csv_arr_src["WriteTransferCount"]))
		csv_arr_dst.KernelModeTime = int(csv_arr_dst.KernelModeTime or 0) + (int(csv_arr_dst.KernelModeTime or 0) - int(csv_arr_src["KernelModeTime"]))
		csv_arr_dst.WorkingSetSize = int(csv_arr_dst.WorkingSetSize or 0) + (int(csv_arr_dst.WorkingSetSize or 0) - int(csv_arr_src["WorkingSetSize"]))
		csv_arr_dst.UserModeTime = int(csv_arr_dst.UserModeTime or 0) + (int(csv_arr_dst.UserModeTime or 0) - int(csv_arr_src["UserModeTime"]))
		csv_arr_dst.ThreadCount = int(csv_arr_dst.ThreadCount or 0) + (int(csv_arr_dst.ThreadCount or 0) - int(csv_arr_src["ThreadCount"]))
		csv_arr_dst.QuotaPeakPagedPoolUsage = int(csv_arr_dst.QuotaPeakPagedPoolUsage or 0) + (int(csv_arr_dst.QuotaPeakPagedPoolUsage or 0) - int(csv_arr_src["QuotaPeakPagedPoolUsage"]))
		csv_arr_dst.Priority = int(csv_arr_dst.Priority or 0) + (int(csv_arr_dst.Priority or 0) - int(csv_arr_src["Priority"]))
		csv_arr_dst.PeakWorkingSetSize = int(csv_arr_dst.PeakWorkingSetSize or 0) + (int(csv_arr_dst.PeakWorkingSetSize or 0) - int(csv_arr_src["PeakWorkingSetSize"]))
		csv_arr_dst.PeakPageFileUsage = int(csv_arr_dst.PeakPageFileUsage or 0) + (int(csv_arr_dst.PeakPageFileUsage or 0) - int(csv_arr_src["PeakPageFileUsage"]))
	csv_arr_dst.employeeUID = csv_arr_src["employeeUID"]
	csv_arr_dst.CreationDate = csv_arr_src["CreationDate"]
	csv_arr_dst.save()
	return csv_arr_dst

def sync_firebase_data():
	all_categories = ProcessCategory.objects.all().exclude(name = "Others")
	firebase, auth = init_fcm_auth()
	db = firebase.database()
	# import pdb; pdb.set_trace()

	employee_tokens = db.child("resource").shallow().get().val()
	resource_per_token_array = []
	print(1)
	# firebase_resource_info = db.child("resource").get().val()
	print(2)
	# import pdb; pdb.set_trace()
	for a_employee_tokens in employee_tokens:
		print(3)
		for a_all_categories in all_categories:
			print(4)
			category_row = CategoryDataPerDay.objects.filter(process_category = a_all_categories, employeeUID = a_employee_tokens)
			resource_val = db.child("resource").child(a_employee_tokens).child("resource_info").get().val()
			if category_row.count() > 0:
				print(5)
				# resource_per_token_array.append(
				# 		{
				# 			"token":a_employee_tokens,
				# 			"resource_info":db.child("resource").child(a_employee_tokens).child("resource_info").get().val(),
				# 		}
				# 	)
				for a_res_from_timestamp in resource_val:
					resource_timestamp = datetime.fromtimestamp(float(a_res_from_timestamp)/100).date()
					resource_timestamp = calendar.timegm(resource_timestamp.timetuple())
					if not category_row.filter(created_at=resource_timestamp).exists():
						# 	perdaycategory = CategoryDataPerDay.objects.filter(process_category = a_all_categories, employeeUID = a_employee_tokens,created_at=resource_timestamp)
						# else:
						perdaycategory = CategoryDataPerDay(process_category = a_all_categories, employeeUID = a_employee_tokens,created_at=resource_timestamp)
						minute_res = db.child("resource").child(a_employee_tokens).child("resource_info").child(a_res_from_timestamp).get().val()
						for a_minute_res in minute_res:
							if a_minute_res.Name in category_row.process_category.all_included_process.split(","):
								pass
			else:
				print(6)
				for a_resource_val in resource_val:
					# import pdb; pdb.set_trace()
					resource_timestamp = datetime.fromtimestamp(float(a_resource_val)/100).date()
					resource_timestamp = calendar.timegm(resource_timestamp.timetuple())
					print(7)
					minute_res = db.child("resource").child(a_employee_tokens).child("resource_info").child(a_resource_val).get().val()
					for a_minute_res in minute_res:
						print(8)
						if a_minute_res["Name"] in a_all_categories.all_included_process.split(","):
							print(9)
							resource_timestamp = datetime.fromtimestamp(float(a_resource_val)/100).date()
							resource_timestamp = calendar.timegm(resource_timestamp.timetuple())
							if CategoryDataPerDay.objects.filter(process_category = a_all_categories, employeeUID = a_employee_tokens, created_at = resource_timestamp).exists():
								category_row = CategoryDataPerDay.objects.get(process_category = a_all_categories, employeeUID = a_employee_tokens, created_at = resource_timestamp)
								category_row = add_or_edit_csvcategory_data(a_minute_res,category_row,"update")
							else:
								category_row = CategoryDataPerDay(process_category = a_all_categories, employeeUID = a_employee_tokens, created_at = resource_timestamp)
								category_row = add_or_edit_csvcategory_data(a_minute_res,category_row,"add")

def run_scripts_csv():
	with open(('./tandp/csvDjango.csv')) as f:
		reader = csv.reader(f)
		next(reader)
		array_of_obj = []
		cate = ProcessCategory.objects.all()
		category_obj = None
		for row in reader:
			pro_name=row[0]
			for a_cate in cate:
				if pro_name in a_cate.description.split(","):
					category_obj = a_cate

			res_final = "".join([i for i in row[4] if i.isdigit()])
			if category_obj:
				category_obj_pk = category_obj.process_key.pk

			else:
				category_obj_pk = ""

			# ReadTransferCount
			# Name
			# WriteTransferCount
			# CreationDate
			# Description
			# KernelModeTime
			# WorkingSetSize
			# UserModeTime
			# ThreadCount
			# QuotaPeakPagedPoolUsage
			# Priority
			# PeakWorkingSetSize
			# PeakPageFileUsage
			# ParentProcessId
			# 

			obj_to_go_in_array = {
				"processName" :row[0],
				"processId" :row[1],
				"resource_amount":res_final,
				"category_pk" : (category_obj_pk)
			}
			# process_det = ProcessDetails.objects.get(process_name = pro_name, process_category= category_obj, is_deleted = False)
			# CsvData.objects.get_or_create( processName = row[0], processId = row[1],resource_amount = res_final , process_key = process_det)
			CsvData.objects.get_or_create( processName = row[0], processId = row[1],resource_amount = res_final )
