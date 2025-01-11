### Setup Instructions

### 1. Clone the repository
Clone the project repository to your local machine:

```bash
git clone https://github.com/yla382/remarcable_project.git
cd remarcable_project
```

### 2. Set Up the .env File
Copy the .env.sample file to .env:
```bash
cp .env.sample .env
```
Update the following with your own (Generate your own secret key using https://www.django-secret-key-generator.com/)
```bash
SECRET_KEY='your_generated_secret_key'
```


### 3. Create and activate a virtual environment
```bash
python3 -m venv venv
```
Activate the virtual environment:

On Windows:
```bash
venv\Scripts\activate
```
On macOS/Linux:
```bash
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Run Migrations
Run database migrations to set up the initial database schema:
```bash
python manage.py migrate
```

### 6. Run the Development Server
```bash
python manage.py runserver
```
You can access the project in your browser by going to http://127.0.0.1:8000.