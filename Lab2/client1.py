import time
import os

LOCK_FILE = "lock-file.txt"
BUFFER_FILE = "buffer.txt"

client_file_name = input("Input response file name:\n")
file_text = input("Input message for server:\n")
running = True

while running:
    if not os.path.exists(LOCK_FILE):
        with open(LOCK_FILE, 'w') as lock_file:
            lock_file.write("lock by client")
            print(f"File '{LOCK_FILE}' created by this client.")

        with open(BUFFER_FILE, 'w') as buffer_file:
            buffer_file.write(f"{client_file_name}\n{file_text}")
            print("Message sent to server.")

        while not os.path.exists(client_file_name):
            print("Waiting for response from server...")
            time.sleep(1)

        with open(client_file_name, 'r') as client_file:
            time.sleep(2)
            response = client_file.read()
            print("Response from server:")
            print(response)

        running = False
    else:
        print("Server is currently unavailable... Please wait.")
        time.sleep(3)
