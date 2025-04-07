import firebase_admin
from firebase_admin import credentials
import configparser
import ast

config = configparser.ConfigParser()
config.read("secrets.ini")
json_key_str = config.get("firebase", "key")
json_key = ast.literal_eval(json_key_str)
cred = credentials.Certificate(json_key)
firebase_admin.initialize_app(cred)