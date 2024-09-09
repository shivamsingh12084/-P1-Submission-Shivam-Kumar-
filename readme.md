# 🚀 RAKT's "Out-of-the-Box" Engineering Challenge 🌟
# 🚚 Food Truck Finder API
A Django-based REST API that provides food truck locations based on latitude and longitude coordinates. The API uses the Haversine formula to calculate the shortest distances between a given point and nearby food trucks.
# 🛠️ Setup Instructions
Clone the Repository
```bash
git clone git@github.com:shivamsingh12084/-P1-Submission-Shivam-Kumar-.git
cd -P1-Submission-Shivam-Kumar-
```
Create virtual environment
For Macos
```bash
python3 -m venv .env
```
For Windowns
```bash
python3 virtualenv.exe .env
```
Activate the Virtual Environment
For Windows:
```bash
.env/Scripts/activate.bat
```
For Macos:
```bash
source .env/bin/activate
```
Install Dependencies
```bash
pip install -r requirements.txt
```
Start the Server
```bash
python manage.py runserver
```
# 🔌 API Documentation
Endpoints:
Main URL: http://127.0.0.1:8000/api/food-trucks/
Parameters: latitude, longitude
Example Request:
Open Postman or type the following URL in your browser:
```bash
http://127.0.0.1:8000/api/food-trucks/?latitude=37.77425926306004&longitude=-122.41948598839828
```

# 🔌 Description
Django ORM is one of the most powerful features and with Django ORM we can very effectively interact with the database to perform custom queries.

So I created a Django project and inside the Django project, I created an app named pages in the models.py of pages I created a model named FoodFacilityPermit and created fields based on the CSV headers provided in the database and migrated the database.

So the first problem is to feed the CSV data in the Django database and by default, Django comes with SQLite database so convert the CSV data into JSON.

We can add the data manually with shell but Django fixtures is a feature to add the dummy data into the database so I formated the JSON data according to models and created a fixtures_data.json inside the pages/fixtures/fixtures_data.json. Now I have added the data into the JSON by "python manage.py loaddata pages/fixtures/fixtures_data.json" and I have added these data into the SQLite database.

Now I want to create a rest API endpoint so we can send latitude and longitude as a parameter with the endpoints urls so I installed Django rest framework on top of Django to create API endpoints, So inside the pages app I created two files first serailizers.py and second urls.py and registered urls in the project main urls.py file then I have created FoodFacilityPermitSerializer inside the serializers.py. Now I have models the data in the database and serializers also so the only thing left is to create views for our endpoints and urls for the endpoints.

In the views.py I have created a function called haversine(The haversine formula determines the great-circle distance between two points on a sphere given their longitudes and latitudes. Important in navigation, it is a special case of a more general formula in spherical trigonometry, the law of haversines, that relates the sides and angles of spherical triangles.) to calculate the distance between two latitudes and longitudes. This function takes def haversine(lat1, lon1, lat2, lon2): two latitudes and longitudes as a parameter and returns the difference between them.

Finally, in the views.py of pages app, I created a class-based function FoodTruckView(APIView) At the start of the function we extracted latitudes and longitudes that the user provided as a parameter, and then I queried all the data from the database(items list) then I have created an array called distance and added all food trucks with respective distance from the given latitude and longitude. Then I sorted the array like the shortest distance at the top and returned the first five elements in the array as JSON data.

# 💡 Potential Improvements
If given more time, I would implement:

Database:

Use Postgres for production readiness.
Add a docker-compose.yml file to configure services (web and database).
Advanced Filters:

Add filters for status, schedule, and approved/not approved fields to get more precise results.
Deployment:

Deploy the API on AWS or any cloud platform for better scalability and availability.
Frontend:

Create a dedicated frontend using React and Next.js for a beautiful UI and a better user experience.

# 🚀 Technologies Used
Django
Django Rest Framework
SQLite








