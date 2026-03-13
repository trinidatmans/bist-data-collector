# Configuration for Database and Logging

DATABASE_SETTINGS = {
    'HOST': 'localhost',
    'PORT': 5432,
    'USER': 'your_db_user',
    'PASSWORD': 'your_db_password',
    'DB_NAME': 'your_db_name'
}

LOGGING_SETTINGS = {
    'LEVEL': 'DEBUG',
    'FORMAT': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'FILENAME': 'app.log'
}