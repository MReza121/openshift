from flask import Flask, jsonify, request, send_file
import os
import csv

app = Flask(__name__)
DATA_DIR = '/etc/mymodel'

# Ensure the data directory exists
# if not os.path.exists(DATA_DIR):
#     os.makedirs(DATA_DIR)

def generate_data():
    # Example function that generates some data
    return [
        ["ID", "Name", "Value"],
        [1, "Alice", 123],
        [2, "Bob", 456],
        [3, "Charlie", 789]
    ]

@app.route('/')
def index():
    return "Welcome to the Flask app running on OpenShift!"

@app.route('/save-function-result', methods=['POST'])
def save_function_result():
    # Generate data from a function
    data = generate_data()
    filename = request.json.get('filename', 'function_result.csv')

    filepath = os.path.join(DATA_DIR, filename)

    try:
        # Save the data to a CSV file
        with open(filepath, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        return jsonify({"message": f"Function result saved to {filename}"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    filepath = os.path.join(DATA_DIR, filename)

    if not os.path.exists(filepath):
        return jsonify({"error": "File not found"}), 404

    try:
        # Send the CSV file to the client
        return send_file(filepath, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
