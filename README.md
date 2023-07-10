# Asset_Tracking_App
Asset Tracking System
This project provides an asset tracking system using Django and Django REST Framework. 
It allows you to manage companies, employees, devices, assets and logs through a RESTful API.

#Features
Companies: Add, update, retrieve, and delete company information.
Employees: Manage employee details and their association with companies.
Devices: Keep track of devices and associate them with companies.
Assets: Track assets assigned to employees, including devices and their condition.
Device Logs: Log and retrieve device condition changes over time.

#Technologies Used
Python
Django
Django REST Framework
SQLite (default database)

#Installation and Setup
1. Clone the repository:
https://github.com/jafrul55/Asset_Tracking_App.git
2. Navigate to the project directory:
cd asset-tracking
3. Install the project dependencies:
pip install -r requirements.txt
4. To migrate SQL code:
python manage.py makemigrations
5. To execute SQL code:
python manage.py migrate
6. Run the development server:
python manage.py runserver

7. Access the application in your web browser:
http://127.0.0.1:8000/

#API Endpoints
The project provides the following API endpoints:

http://127.0.0.1:8000//api/companies/: CRUD operations for companies.
http://127.0.0.1:8000//api/employees/: CRUD operations for employees.
http://127.0.0.1:8000//api/devices/: CRUD operations for devices.
http://127.0.0.1:8000//api/assets/: CRUD operations for assets.
http://127.0.0.1:8000//api/devicelog/: CRUD operations for device logs.

For Admin:
created Superuser:
username:root
email:root@gmail.com
password:12345

#I hope this instruction and facilities will help you to use and understand the project features easily. I give my best to make this app user-friendly.
Thank You so much!




