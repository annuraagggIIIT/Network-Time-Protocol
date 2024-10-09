from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Function to log data and compare timestamps
def log_and_compare(client_name, client_timestamp):
    server_timestamp = datetime.utcnow()
    client_time_obj = datetime.strptime(client_timestamp, '%Y-%m-%dT%H:%M:%S.%f')
    
    # Calculate time difference
    time_diff = abs((server_timestamp - client_time_obj).total_seconds())
    max_allowed_diff = 5  # Max difference allowed in seconds
    
    if time_diff <= max_allowed_diff:
        result = "Timestamps match within the allowed range."
    else:
        result = "Timestamps do not match."
    
    return {
        "client_name": client_name,
        "client_timestamp": client_timestamp,
        "server_timestamp": server_timestamp.isoformat() + ' UTC',
        "time_difference": time_diff,
        "result": result
    }

@app.route('/submit-data', methods=['POST'])
def receive_data():
    data = request.json
    client_name = data.get('name')
    client_timestamp = data.get('timestamp')
    
    # Log and compare the timestamps
    result = log_and_compare(client_name, client_timestamp)
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
