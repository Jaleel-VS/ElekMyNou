import firebase_admin
from firebase_admin import credentials, firestore
import os

currentdir = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(currentdir, "config.json")

class Database:
    __instance = None

    @staticmethod
    def getInstance():
        if Database.__instance == None:
            Database()
        return Database.__instance
    
    def __init__(self):
        self.db = None
        Database.__instance = self
        self.__initFirebase()

    def __initFirebase(self):
        cred = credentials.Certificate(config_path)
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def get_db_object(self):
        return self.db

if __name__ == "__main__":
    db = Database.getInstance()
    print(db.db)

