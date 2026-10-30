# Lab2-UDP

## Overview

This project implements a UDP Ping client in Python. The client sends 10 ping requests to a UDP server and measures the round-trip time (RTT) for each successful response.

The server randomly drops incoming packets to simulate packet loss. The client uses a one-second timeout to detect missing responses and displays "Request timed out" when no response is received.

## Project Structure

```text
Lab2-UDP/
├── UDPPingerServer.py
├── UDPPingerClient.py
└── README.md
```

## Requirements

- Python 3

## How to Run

**1. Start the UDP server**

Open a terminal and run:

```bash
python3 UDPPingerServer.py
```

The server listens on port `12000`.

**2. Run the UDP client**

Open a second terminal, navigate to the project directory, and run:

```bash
python3 UDPPingerClient.py
```

## Expected Output

The client sends 10 ping requests and displays the server response and RTT for successful requests. If a response is not received within one second, it displays:

```text
Request timed out
```

The results may vary between executions because the server randomly drops packets.
