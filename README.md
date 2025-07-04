# 🏋️‍♂️ Fitness Studio Booking API

A simple and clean RESTful API for a fictional fitness studio. Clients can view fitness classes and book a spot in available sessions.

> Built with Django, Django REST Framework, and SQLite (in-memory), with focus on clean code, modular structure, input validation, timezone handling, and unit testing.

---

## 📚 Features

- 📅 View all upcoming fitness classes (`GET /api/classes/`)
- 📥 Book a fitness class (`POST /api/booking/`)
- 📧 View bookings made by a specific email (`GET /api/bookings/email/`)
- ⏰ Handles timezone (IST) with automatic conversion
- 🚫 Prevents overbooking and missing required fields
- ✅ Unit tested with Django’s built-in test framework
- 🧪 In-memory SQLite DB (no setup required)

---

## 🔧 Setup Instructions
Follow these steps to run the project locally:

# STEP 1
### 1. Clone the Repository
```bash
git clone https://github.com/your-username/fitnessstudio-booking-api.git
cd fitnessstudio-booking-api

# STEP 2
# Create virtual environment
python -m venv env
# Activate the environment
# On Windows:
env\Scripts\activate
# On macOS/Linux:
source env/bin/activate

# STEP 3
# Install Dependencies
pip install -r requirements.txt

# STEP 4
Run Migrations
python manage.py makemigrations
python manage.py migrate

#STEP 5
Sample Data
# In bash
python manage.py shell

--paste this

from fitnessapi.models import FitnessClass
from django.utils.timezone import now, timedelta

FitnessClass.objects.create(
    name='Yoga',
    instructor='Alex',
    datetime=now() + timedelta(days=1),
    total_slots=10,
    available_slots=10
)

FitnessClass.objects.create(
    name='Zumba',
    instructor='Ben',
    datetime=now() + timedelta(days=2),
    total_slots=15,
    available_slots=15
)

FitnessClass.objects.create(
    name='HIIT',
    instructor='Mia',
    datetime=now() + timedelta(days=3),
    total_slots=10,
    available_slots=10
)

--exit the shell
exit()

#start the server 
python manage.py runserver

#sample API Request on Postman
-View All classes
method-GET
URL:http://127.0.0.1:8000/api/classes/
-Book a Class
method-POST
URL:http://127.0.0.1:8000/api/booking/
--Body--
The fitness_class ids changes according to classes from the get we can see the class ids 
{
  "fitness_class": 1,
  "client_name": "Name",
  "client_email": "email@example.com"
}

-View Bookings By Email
method-GET
URL:http://127.0.0.1:8000/api/bookings/email@example.com/

#Run Unit Tests
-bash
python manage.py test
