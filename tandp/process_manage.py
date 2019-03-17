import threading 
import subprocess, sys
import os

def printit():
	threading.Timer(1000.0,printit).start()
	#subprocess.run(r'''tasklist /FO csv > csvDjango.csv''', shell = True)
	#print("hell")
	#subprocess.run(r'''wmic process where processId=37960 list /format''' , shell = True)
	subprocess.Popen('powershell.exe [New-TimeSpan -Start (get-process sublime_text).StartTime | Export-Csv dmfvf.csv]')
	

def powershell_sc():
        subprocess.Popen(["powershell.exe","C:\\Users\\hp\\Documents\\django-timeandproductivity\\ps .ps1"],stdout = sys.stdout)
        

printit()
