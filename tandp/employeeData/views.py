from django.shortcuts import render
import pyrebase
import csv, pytz, json, calendar, urllib
from django.utils import timezone
from csvReader.models import *
from django.http import HttpResponse
from employeeData.functions import *
from users.models import *
import numpy as np
import pandas as pd
from datetime import datetime
#from django.http import HttpResponse
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def create_new_user(request):
	firebase , auth = init_fcm_auth()
	email = "username2@user.com"
	password = "password123"
	# import pdb; pdb.set_trace()
	try:
		succ_res = auth.create_user_with_email_and_password(email, password)
	except Exception as excp:
		# pdb.set_trace()
		x, y = excp.args
		exp_obj = json.loads(y)
		exception_response = exp_obj["error"]
		return HttpResponse(exception_response["message"])

	else:
		# pdb.set_trace()
		return HttpResponse(succ_res["localId"] + "-" + succ_res["idToken"])



def authconnect(request):
	firebase, token = get_fcm_token()
	db = firebase.database()
	terminal_resource = [
							{"processId":"123456","processName":"chrome.exe","resource_amount":"12345"},
							{"processId":"123457","processName":"setupvhc.exe","resource_amount":"12347"},
							{"processId":"123458","processName":"setupvlc.exe","resource_amount":"12348"},
							{"processId":"123458","processName":"vivwk.exe","resource_amount":"12348"},
							{"processId":"123458","processName":"cc.exe","resource_amount":"12348"},
						]
	data = {
		"csvdata": terminal_resource
	}

	tz = pytz.timezone('Asia/Kolkata')
	time_stamp_val = int(datetime.datetime.now(timezone.utc).astimezone(tz).timestamp() * 100)
	# import pdb; pdb.set_trace()
	# dt = datetime.datetime.fromtimestamp(time_stamp_val/100, tz).strftime('%Y-%m-%d %H:%M:%S')
	res = db.child("resource").child(token).child("resource_info").child(time_stamp_val).set(terminal_resource)
	return HttpResponse(token)

def read_process_detail(request):
	with open(('./tandp/csvDjango.csv')) as f:
		reader = csv.reader(f)
		for row in reader:
			_, created = Category.objects.get_or_create(
                processId=row[0],
                processName=row[1],
                resource_amount=row[2],
                )
	# with open(('./tandp/newtask.csv')) as f:
	# 	reader = csv.reader(f)
	# 	col1 = []
	# 	col2 = []
	# 	import pdb; pdb.set_trace()
	# 	for row in reader:
			# pass
			# col1.append(row[0])
			# col2.append(row[1])

	return "Hello"


def process_data(request):
	listToAdd = ['chrome.exe','sublime_text.exe','notepad++.exe','pythonw.exe','EXCEL.EXE',]
	emptylist =[]
	with open(('./tandp/csvDjango.csv')) as f:
		reader = csv.reader(f)
		next(reader)
		context={
		"name": "SIH"
		}
		for row in reader:
			# "12,321"
			res_final = "".join([i for i in row[4] if i.isdigit()])
			# res_final = ""
			# for a_str_res in str_res:
			# 	if a_str_res.isdigit():
			# 		res_final += a_str_res
			_, created = CsvData.objects.get_or_create( processName = row[0], processId = row[1],resource_amount = res_final )
	return render(request,'employeeData/employee_data.html',context)

def view_chart(request):
	# import pdb; pdb.set_trace()
	all_categories = ProcessCategory.objects.all().exclude(name = "Others")
	all_category = []
	all_resource_array = []
	for a_all_categories in all_categories:
		sum_of_all = 0
		all_csv_data_per_day = CategoryDataPerDay.objects.filter(process_category = a_all_categories)
		for a_all_csv_data_per_day in all_csv_data_per_day:
			sum_of_all += int(a_all_csv_data_per_day.KernelModeTime or 0)

		if not a_all_categories.name in all_category:
			all_category.append(a_all_categories.name)
				# max_val_category = 0
				# max_val_category = int(a_all_csv_data_per_day.KernelModeTime)
		all_resource_array.append(sum_of_all)
			#### maybe next time proper eval
			# if int(a_all_csv_data_per_day.KernelModeTime) > max_val_category:
			# 	max_val_category = int(a_all_csv_data_per_day.KernelModeTime)
			# 	all_resource_array.append(max_val_category)
	# for a_all_categories in all_categories:
		# employee_tokens_array.append(a_employee_tokens)
	max_resource_val = max(all_resource_array)
	all_resource_array = np.array(all_resource_array)
	all_resource_array = np.divide(all_resource_array, max_resource_val)
	all_resource_array = np.around(all_resource_array.astype(np.double), decimals=2)
	firebase, auth = init_fcm_auth()
	db = firebase.database()
	tokens = db.child("resource").shallow().get().val()
	tokens = [x for x in tokens]

	# all_category = ['a','b','c','d']
	# all_resource_array = [1,2,3,4]
	# import pdb;pdb.set_trace() 
	context = {
		"all_memory_array" : json.dumps(list(all_resource_array)) ,
		"all_process" : ",".join(all_category),
		"tokens" : ",".join(tokens)
	}
	if not request.method == "POST":
		return render(request,'employeeData/data.html',context)
	else:
		# date_var = 
		return render(request,'employeeData/data.html',context)

def view_chart_custom(request):
	#date_var=request.POST.get('date')
	date_var = "2019_03_17"
	#token = "nd1vevEB3HPPoxsklORsEl8XBGy2"
	token=request.POST.get('UniqueEmployee')
	#token = token_selected
	date_var = date_var.split("_")
	date_var = "-".join(date_var)
	date_var = datetime.strptime(date_var,'%Y-%M-%d').date()
	calendar.timegm(date_var.timetuple())
	token = token
	#import pdb; pdb.set_trace()
	all_categories = ProcessCategory.objects.all().exclude(name = "Others")
	all_category = []
	all_resource_array = []
	for a_all_categories in all_categories:
		sum_of_all = 0
		if not token == "Unset":
			all_csv_data_per_day = CategoryDataPerDay.objects.filter(process_category = a_all_categories, employeeUID = token)
		if not date_var == "Unset":
			all_csv_data_per_day = CategoryDataPerDay.objects.filter(process_category = a_all_categories,employeeUID = token)
		for a_all_csv_data_per_day in all_csv_data_per_day:
			sum_of_all += int(a_all_csv_data_per_day.KernelModeTime or 0)

		if not a_all_categories.name in all_category:
			all_category.append(a_all_categories.name)
				# max_val_category = 0
				# max_val_category = int(a_all_csv_data_per_day.KernelModeTime)
		all_resource_array.append(sum_of_all)
			#### maybe next time proper eval
			# if int(a_all_csv_data_per_day.KernelModeTime) > max_val_category:
			# 	max_val_category = int(a_all_csv_data_per_day.KernelModeTime)
			# 	all_resource_array.append(max_val_category)
	# for a_all_categories in all_categories:
		# employee_tokens_array.append(a_employee_tokens)
	print (all_resource_array[2])
	max_resource_val = max(all_resource_array)
	divide_val = max_resource_val/10000
	for y in all_resource_array:
		if y==max_resource_val:
			all_resource_array[all_resource_array.index(y)] /=  10000000 or 0
		else:
			all_resource_array[all_resource_array.index(y)] /= 100
	print(all_resource_array)
	print(abs(all_resource_array[0]))
	o=6.998765
	print(int(o))
	#all_resource_array = np.array(all_resource_array)
	#all_resource_array = np.divide(all_resource_array, max_resource_val/100)
	#all_resource_array = np.around(all_resource_array.astype(np.double), decimals=2)
	firebase, auth = init_fcm_auth()
	db = firebase.database()
	tokens = db.child("resource").shallow().get().val()
	tokens = [x for x in tokens]

	

    
	# all_category = ['a','b','c','d']
	# all_resource_array = [1,2,3,4]
	# import pdb;pdb.set_trace() 
	context = {
		"all_memory_array" : abs(int(all_resource_array[0])) ,
		"all_memory_array2" : abs(int(all_resource_array[1])) ,
		"all_memory_array3" : abs(int(all_resource_array[2])),
		"all_memory_array4" : abs(int(all_resource_array[3])),


		"all_process" : ",".join(all_category),
		"tokens" : ",".join(tokens)
	}
	return render(request,'employeeData/data.html',context)

    
def predict_next_month_performance(request):
	# import pdb; pdb.set_trace()
	all_categories = ProcessCategory.objects.all().exclude(name = "Others")
	total_array = []
	array_of_labels = []
	array_of_data = []
	for a_all_categories in all_categories:
		if CsvData.objects.filter(process_category = a_all_categories).count() > 0:
			lpp = pd.DataFrame(list(CsvData.objects.filter(process_category = a_all_categories).values("KernelModeTime","created_at")))
			cppb = lpp.apply(pd.to_numeric,errors='coerce')
			cppb = cppb.dropna()
			x_axis = cppb.iloc[:,:1].values
			y_axis = cppb.iloc[:,1:].values
			regressor = LinearRegression()
			# X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 1/3, random_state = 5)
			regressor.fit(x_axis, y_axis)
			regressor.score(x_axis, y_axis)
			# y_pred = regressor.predict(X_test) 
			tempX = ",".join([str(x) for x in x_axis.ravel()])
			tempY = ",".join([str(y) for y in y_axis.ravel()])
			context = {
				"X" : tempX,
				"Y" : tempY,
			}
			# array_of_labels.append(a_all_categories.name)
			# array_of_data.append(context)
			total_array.append(
				{
				"Label":a_all_categories.name,
				"Data":context
				}
			)
	context = {
		# "array_of_labels" : json.dumps(array_of_labels),
		# "array_of_data": json.dumps(array_of_data),
		"total_array":json.dumps(total_array)
	}
		# import pdb;pdb.set_trace()
	# return HttpResponse(regressor.score(X_test, y_pred))
	return render(request,'employeeData/predict_data.html',context)

	# return render(request,'employeeData/data.html',context)


def update_graph(request):
	sync_firebase_data();
	
	return render(request,'employeeData/data.html')






























# categories_per_day = CategoryDataPerDay.objects.all().order_by('-pk')
	# unique_categories = []
	# all_resource_array = []
	# all_category = []
	# for a_all_categories in all_categories:
	# 	category_objs = categories_per_day.filter(process_category = a_all_categories)
	# 	all_category.append(a_all_categories.name)
	# 	category_resource_total = 0
		
	# 	for a_categories_per_day in category_objs:
	# 		category_resource_total += int(a_categories_per_day.KernelModeTime)
	# 	all_resource_array.append(category_resource_total)

	# for a_emp_data in emp_data:
	# 	if a_emp_data.processName not in all_process:
	# 		all_memory_array.append(a_emp_data.resource_amount)
	# 		all_process.append(a_emp_data.processName)

	# all_data_obj = []
	# import pdb; pdb.set_trace()
	# memory_arr = ",".join(all_memory_array)
	#  process_arr = ",".join(all_process)

		# "all_process" : json.dumps(all_category)
