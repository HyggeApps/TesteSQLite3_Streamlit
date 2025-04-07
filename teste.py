import firebase_admin
from firebase_admin import credentials

json_key = ["firebase"]["key"]
cred = credentials.Certificate(json_key)
firebase_admin.initialize_app(cred)