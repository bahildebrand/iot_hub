import pyrebase
import json


class DataBase:
    def __init__(self):
        config = json.load(open("config.json"))
        firebase = pyrebase.initialize_app(config["database"])
        auth = firebase.auth()
        login = config["login"]
        self.user = auth.sign_in_with_email_and_password(login["username"],
                                                         login["password"])

        self.db = firebase.database()

    def push(self, sensor_name, data_record):
        self.db.child("sensors").child(sensor_name).push(data_record,
                                                         self.user['idToken'])
