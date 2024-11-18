import os
import signal
import sys
import time
import threading

MAX_PATH_LENGTH = 20
FIFO_SERVER = "/tmp/server_fifo"

database = {
    1: "Kowalski",
    2: "Nowak",
    3: "Wiśniewski"
}


def handle_signals(sig, frame):
    if sig == signal.SIGHUP or sig == signal.SIGTERM:
        print("Signal ignored.")
    elif sig == signal.SIGUSR1:
        print("SIGUSR1 received. Server stopped.")
        sys.exit(0)


# set signal handling
signal.signal(signal.SIGHUP, handle_signals)
signal.signal(signal.SIGTERM, handle_signals)
signal.signal(signal.SIGUSR1, handle_signals)


def handle_client_request(data):
    # message_length = int.from_bytes(data[:4], 'little')
    client_id = int.from_bytes(data[4:8], 'little')
    client_path = data[8:8 + MAX_PATH_LENGTH].decode('utf-8').strip('\x00')

    print(f"Message received from {client_path}")

    response = database.get(client_id, "Nie ma")

    time.sleep(2)

    with open(client_path, "wb") as client_fifo:
        response_data = response.encode('utf-8')
        message_length = len(response_data)
        client_fifo.write(message_length.to_bytes(4, 'little') + response_data)
    print(f"Response sent to {client_path}")


if not os.path.exists(FIFO_SERVER):
    os.mkfifo(FIFO_SERVER)

print("Server is running...")

while True:
    with open(FIFO_SERVER, "rb") as server_fifo:
        data = server_fifo.read()
        if not data:
            continue

        client_thread = threading.Thread(target=handle_client_request, args=(data,))
        client_thread.start()