from firebase import firebase

firebase = firebase.FirebaseApplication('https://console.firebase.google.com/u/2/project/sihtheemdb/database/sihtheemdb/data')

result = firebase.get('resource',None)
print(result)
