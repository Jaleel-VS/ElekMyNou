from db.main import Database
from models import Voter, Candidate

class UserService:
    def __init__(self):
        self.db = Database()

    def create_voter(self, voter: Voter):
        self.db.collection('voters').add(voter.to_dict())

    def create_candidate(self, candidate: Candidate):
        self.db.collection('candidates').add(candidate.to_dict())

    def get_all_voters(self):
        return self.db.collection('voters').get()
    
    def get_all_candidates(self):
        return self.db.collection('candidates').get()
    
    def get_voter(self, voter_id: str):
        return self.db.collection('voters').document(voter_id).get()
    
    def get_candidate(self, candidate_id: str):
        return self.db.collection('candidates').document(candidate_id).get()
    
