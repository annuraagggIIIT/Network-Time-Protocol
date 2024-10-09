import requests
from datetime import datetime, timedelta

# func to collect user input and send to server
def submit_data(spoof=False):
    name = input("Enter your name: ")
    
    if spoof:
        # Spoofed timestamp: 1 hour into the past
        client_timestamp = (datetime.utcnow() - timedelta(hours=1)).isoformat()
        print(f"Sending Spoofed Timestamp: {client_timestamp} UTC")
    else:
        # correct timestamp: current UTC time
        client_timestamp = datetime.utcnow().isoformat()
        print(f"Client Timestamp: {client_timestamp} UTC")
    
    # prepare data to send
    data = {
        "name": name,
        "timestamp": client_timestamp
    }
    
    # Sennd data to the server
    response = requests.post('http://localhost:5000/submit-data', json=data)
    
    if response.status_code == 200:
        print("Server Response:")
        print(response.json())
    else:
        print("Failed to get a valid response from the server.")

if __name__ == "__main__":
    spoof_data = input("Do you want to spoof the timestamp? (yes/no): ").lower()
    if spoof_data == 'yes':
        submit_data(spoof=True)
    else:
        submit_data(spoof=False)
