# app.py
from flask import Flask
import os

# Define the path where the PVC is mounted
mount_path = '/MODEL_PATH1'
file_path = os.path.join(mount_path, 'example.txt')

# Data to be written
data = 'Hello, OpenShift PVC!'

# Write data to the file
with open(file_path, 'w') as file:
    file.write(data)

print(f'Data has been written to {file_path}')









app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, OpenShift with Docker!'

@app.route('/')
def hello_world():
    return 'Hello, OpenShift with Docker!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)