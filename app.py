import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return {
        'status': 'ok',
        'db_password': os.environ.get('DB_PASSWORD', 'not-set'),
        'api_key': os.environ.get('API_KEY', 'not-set'),
        'secret_token': os.environ.get('SECRET_TOKEN', 'not-set')
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
