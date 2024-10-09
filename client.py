import requests
from datetime import datetime

# func to collect user input and send to server
def submit_data():
    name = input("Enter your name: ")
    client_timestamp = datetime.utcnow().isoformat()
    
    # Prepare data to send
    data = {
        "name": name,
        "timestamp": client_timestamp
    }
    
    print(f"Client Timestamp: {client_timestamp} UTC")
    
    # Send data to the server
    response = requests.post('http://localhost:5000/submit-data', json=data)
    
    if response.status_code == 200:
        print("Server Response:")
        print(response.json())
    else:
        print("Failed to get a valid response from the server.")

if __name__ == "__main__":
    submit_data()
