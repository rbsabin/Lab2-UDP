
# UDPPingerClient.py

import time
from socket import *

# Server details
serverName = '127.0.0.1'
serverPort = 12000

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Set socket timeout to one second
clientSocket.settimeout(1)

print("UDP Ping Client Started")
print(f"Sending 10 ping requests to {serverName}:{serverPort}\n")

for sequence_number in range(1, 11):

    # Create the ping message
    send_time = time.time()
    message = f"Ping {sequence_number} {send_time}"

    # Record the start time and send the message
    start_time = time.perf_counter()
    clientSocket.sendto(message.encode(), (serverName, serverPort))

    try:
        # Wait for the server response
        response, serverAddress = clientSocket.recvfrom(1024)

        # Calculate round-trip time
        end_time = time.perf_counter()
        rtt = end_time - start_time

        # Display the response and RTT
        print(f"Reply from {serverAddress[0]}: {response.decode()}")
        print(f"Round-trip time: {rtt:.6f} seconds\n")

    except timeout:
        # Display timeout message if no response arrives
        print("Request timed out\n")

# Close the socket
clientSocket.close()

print("UDP Ping Client Finished")

