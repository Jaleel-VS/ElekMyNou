from firebase_admin import auth
from faker import Faker
from db.main import Database
from models import User
from auth import hash_password
import random
from datetime import datetime, timedelta



# Initialize Faker
fake = Faker()

# get db object
db = Database.getInstance().get_db_object()

# Function to create user in Firebase Authentication
def create_user(email, password):
    try:
        user = auth.create_user(
            email=email,
            password=password
        )
        print(f"User {email} created successfully")
        return user.uid
    except Exception as e:
        print(f"Error creating user: {e}")

def generate_sa_id_number(min_age=18, max_age=72):
    # Generate a random birthdate for a person aged between 'min_age' and 'max_age'
    today = datetime.today()
    earliest_birthdate = today - timedelta(days=365 * max_age)
    latest_birthdate = today - timedelta(days=365 * min_age)
    birthdate = earliest_birthdate + timedelta(days=random.randint(0, (latest_birthdate - earliest_birthdate).days))
    birthdate_str = birthdate.strftime("%y%m%d")

    # Generate a random sequence of digits for the rest of the ID number
    sequence = ''.join(str(random.randint(0, 9)) for _ in range(6))

    # Combine birthdate and sequence to form the initial ID number
    id_number = birthdate_str + sequence

    # Calculate the checksum digit using the Luhn algorithm
    checksum = 0
    for i, digit in enumerate(id_number):
        if i % 2 == 0:
            checksum += int(digit)
        else:
            checksum += sum(int(x) for x in str(int(digit) * 2))
    checksum = (10 - (checksum % 10)) % 10

    # Append the checksum to complete the ID number
    id_number += str(checksum)

    return id_number


def get_random_province():
    provinces = ["GP", "KZN", "WC", "EC", "LP", "MP", "NW", "FS", "NC"]
    # Population data for each province (2022 census)
    province_population = {
        "GP": 15099422,
        "KZN": 12423907,
        "WC": 7433019,
        "EC": 7230204,
        "LP": 6572720,
        "MP": 5143324,
        "NW": 3804548,
        "FS": 2745590,
        "NC": 1355946
    }
    # Calculate weights based on population (higher population, higher weight)
    total_population = sum(province_population.values())
    weights = [province_population[province] / total_population for province in provinces]
    # Select province based on weighted probabilities
    chosen_province = random.choices(provinces, weights=weights)[0]
    return chosen_province

def get_random_email_domain():
    domains = ["gmail.com", "yahoo.com", "outlook.com", "icloud.com", "protonmail.com", "aol.com", "zoho.com", "yandex.com", "mail.com", "gmx.com"]
    
    return random.choice(domains)

for _ in range(250):
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = first_name.lower()[0] + last_name.lower() + str(random.randint(100, 999)) + "@" + get_random_email_domain()
    password = fake.password()
    user_id = create_user(email, password)
    province = get_random_province()
    nationalID = generate_sa_id_number()
    user = User(user_id=user_id, first_name=first_name, last_name=last_name, email=email, province=province, nationalID=nationalID, password=hash_password(password))

    db.collection('voters').document(user_id).set(dict(user))
