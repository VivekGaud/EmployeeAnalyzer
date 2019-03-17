from pathlib import Path
import sys, platform, json, random, calendar, pytz
import pyrebase , wmi, pythoncom
from datetime import datetime, timezone
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

firebase = pyrebase.initialize_app(FCMCONFIG)
auth = firebase.auth()

HOME_PATH = str(Path.home())
HOME_PATH = HOME_PATH.replace('\\','_')
HOME_PATH = HOME_PATH.replace(':','-')
temp_str = "".join([random.choice("abcdefghijklmnopqrstuvwxyz1234567890") for i in range(10)])
HOME_PATH = HOME_PATH + temp_str
# company_UID
HOME_PATH = HOME_PATH.upper()
username = HOME_PATH + "@company.com"
password = "company"
json_data={
	"username":username,
	"password":password
}
with open('login_cred.json', 'w') as outfile:
    json.dump(json_data, outfile)

try:
	succ_res = auth.create_user_with_email_and_password(username, password)
except Exception as excp:
	import pdb;pdb.set_trace()
	x, y = excp.args
	exp_obj = json.loads(y)
	exception_response = exp_obj["error"]
	raise_error = True
else:
	raise_error = False