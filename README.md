# Remind-me-later

## Project Overview

The **Remind-me-later** web application allows users to set reminders with a custom message, specifying the date and time for the reminder. This application supports reminders through **SMS** and **Email** (other methods may be added in the future). The main objective of this project is to provide an API endpoint that stores reminder details (date, time, message, reminder method) in the database.

### Key Features

- **Reminder Setup:** Users can set reminders by providing:
  - Date
  - Time
  - Message
  - Reminder method (SMS or Email)
  
- **API Endpoints:**
  - POST `/api/reminders/` to create a new reminder.

- **Database Storage:** Reminders are stored in a database (SQLite by default).

### Task Requirements

1. **Create an API Endpoint:**
   - The API should accept a POST request with the following data:
     - Date
     - Time
     - Message
     - Reminder method (SMS, Email)
   
2. **Store the Reminder:**
   - Store the reminder data in a database (SQLite or another database of choice).
   
3. **No Message Delivery Logic:** 
   - You do not need to implement the actual message delivery via SMS/Email, just store the reminders.

4. **Framework:** 
   - Use **Django** for creating the API endpoint. If you're unfamiliar with Django, you may use any other Python framework of your choice (e.g., Flask, FastAPI).

---

## Tech Stack

- **Backend Framework:** Django
- **Database:** SQLite (default for development)
- **API Framework:** Django REST Framework
- **Python Version:** Python 3.x

---

## Installation Guide

### Prerequisites

- Python 3.x
- Django 4.x or later
- Django REST Framework

### Steps to Set Up Locally

1. **Clone the Repository:**
   Clone the repository to your local machine.

   ```
   git clone https://github.com/your-username/remind-me-later.git
   
2. Navigate to the Project Folder:
```
cd remind-me-later
```
3. Create and Activate a Virtual Environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
4. Install Dependencies:

Install the required dependencies using pip.
pip install -r requirements.txt

5. Apply Database Migrations:

Run the following command to apply migrations and set up the database.

python manage.py migrate

6. Run the Development Server:
Start the Django development server.

python manage.py runserver

7. Access the API:

Visit http://127.0.0.1:8000/ to access the API.

API Endpoints
1. Create a Reminder
URL: /api/reminders/

Method: POST

Description: Accepts reminder details and stores them in the database.

Request Body:
json

{
  "date": "2025-05-15",
  "time": "15:30",
  "message": "Meeting reminder",
  "reminder_method": "SMS"
}
date: The date for the reminder.

time: The time for the reminder.

message: The reminder text message.

reminder_method: The method of reminder (either "SMS" or "Email").

Response:
json

{
  "id": 1,
  "date": "2025-05-15",
  "time": "15:30",
  "message": "Meeting reminder",
  "reminder_method": "SMS"
}
Success Response:

Code: 201 CREATED

Content: The reminder has been successfully saved.

Error Response:

Code: 400 BAD REQUEST

Content: If the provided data is invalid, an error message will be returned.
