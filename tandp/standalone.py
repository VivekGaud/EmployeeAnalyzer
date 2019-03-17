from pathlib import Path
import sys, platform, json, random, calendar, pytz
import pyrebase , wmi, pythoncom
from datetime import datetime, timezone
# username = "C-_USERS_HPM8HB8U9HYA@company.com"
import pdb; pdb.set_trace()
json_data=open("login_cred.json").read()
data = json.loads(json_data)
username = data["username"]
password = data["password"]
OS_NAME = platform.system()
HOME_PATH = ""
FCMCONFIG = {
	'apiKey': 'AIzaSyD7cbYffsmVLzcnsjnBzBB9ednuoHAu4SA',
	'authDomain': 'sihtheemdb.firebaseapp.com',
	'databaseURL': 'https://sihtheemdb.firebaseio.com',
	'projectId': 'sihtheemdb',
	'storageBucket': 'sihtheemdb.appspot.com',
	'messagingSenderId': '446405373476'
}

def init_fcm_auth():
	firebase = pyrebase.initialize_app(FCMCONFIG)
	auth = firebase.auth()
	return firebase,auth

if OS_NAME == 'Windows':
	HOME_PATH = str(Path.home())
	HOME_PATH = HOME_PATH.replace('\\','_')
	HOME_PATH = HOME_PATH.replace(':','-')
	temp_str = "".join([random.choice("abcdefghijklmnopqrstuvwxyz1234567890") for i in range(10)])
	HOME_PATH = HOME_PATH + temp_str
	# company_UID
	HOME_PATH = HOME_PATH.upper()
	# username = HOME_PATH + "@company.com"
	# password = "company"
	print(username,password)
	firebase,auth = init_fcm_auth()
	raise_error = False
	# import pdb; pdb.set_trace()
	try:
		# succ_res = auth.create_user_with_email_and_password(username, password)
		succ_res = auth.sign_in_with_email_and_password(username, password)
	except Exception as excp:
		x, y = excp.args
		exp_obj = json.loads(y)
		exception_response = exp_obj["error"]
		raise_error = True
	else:
		raise_error = False

	if raise_error:
		print(exception_response["message"])
	else:
		print("Success")
		token = succ_res["localId"]
		pythoncom.CoInitialize()
		c = wmi.WMI()
		proc = c.Win32_Process()
		firebase_array = []
		for process in proc:
			process_image = {
				"ReadTransferCount": process.ReadTransferCount,
				"Name": process.Name,
				"WriteTransferCount": process.WriteTransferCount,
				"CreationDate": process.CreationDate,
				"Description": process.Description,
				"KernelModeTime": process.KernelModeTime,
				"WorkingSetSize": process.WorkingSetSize,
				"UserModeTime": process.UserModeTime,
				"ThreadCount": process.ThreadCount,
				"QuotaPeakPagedPoolUsage": process.QuotaPeakPagedPoolUsage,
				"Priority": process.Priority,
				"PeakWorkingSetSize": process.PeakWorkingSetSize,
				"PeakPageFileUsage": process.PeakPageFileUsage,
				"ParentProcessId": process.ParentProcessId,
				"created_at":calendar.timegm(datetime.now().date().timetuple()),
				"employeeUID": token
			}
			firebase_array.append(process_image)
		# pdb.set_trace()
		tz = pytz.timezone('Asia/Kolkata')
		time_stamp_val = int(datetime.now(timezone.utc).astimezone(tz).timestamp() * 100)
		db = firebase.database()
		db.child("resource").child(token).child("resource_info").child(time_stamp_val).set(firebase_array)
		print("Done")
