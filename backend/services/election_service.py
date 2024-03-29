from models import Election
from db.main import Database

class ElectionService:
    def __init__(self):
        self.db = Database.getInstance().get_db_object()

    def create_election(self, election: Election):
        self.db.collection('elections').document(election.election_id).set(dict(election))

    def get_all_elections(self):
        return self.db.collection('elections').get()
    
    def get_election(self, election_id: str):
        return self.db.collection('elections').document(election_id).get()
    
   