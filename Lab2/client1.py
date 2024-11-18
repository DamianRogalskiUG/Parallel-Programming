import time
import os
import errno


LOCK_FILE = "lock-file.txt"
BUFFER_FILE = "buffer.txt"

client_file_name = input("Input response file name:\n")
file_text = input("Input message for server:\n")
running = True

while running:
    try:
        #Open file exclusively
        fd = os.open(LOCK_FILE, os.O_CREAT|os.O_EXCL|os.O_RDWR)
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

        os.close(fd)
        os.remove(LOCK_FILE)
        running = False
    except OSError as e:
        if e.errno == errno.EEXIST:
            # Gdy `lockfile` już istnieje
            print("Server is currently unavailable... Please wait.")
            time.sleep(3)
        else:
            running = False

