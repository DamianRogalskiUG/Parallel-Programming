import os
import time

BUFFER_FILE = "buffer.txt"
LOCK_FILE = "lock-file.txt"


def server_loop():
    while True:
        time.sleep(1)
        print("Server loop")
        if not os.path.exists(LOCK_FILE):
            time.sleep(1)
            continue

        with open(BUFFER_FILE, 'r') as buf:
            lines = buf.readlines()
            client_response_file = lines[0].strip()
            client_message = "".join(lines[1:]).strip()
            print(f"Serwer otrzymał wiadomość od klienta:\n{client_message}")

            with open(client_response_file, 'w') as client_file:
                client_file.write(client_message)

        print(f"Odpowiedź została wysłana do klienta w pliku {client_response_file}.")

        time.sleep(1)


if __name__ == "__main__":
    print("Serwer uruchomiony. Oczekiwanie na wiadomości...")
    server_loop()
