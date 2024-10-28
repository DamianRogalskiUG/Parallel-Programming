# import time
# import os
#
#
# running = True
#
# BUFFER_FILE = "server-buffer.txt"
# LOCK_FILE = "lock-file.txt"
#
# while running:
#     if not os.path.exists(LOCK_FILE):
#         time.sleep(1)
#         print("Lock file exists")
#         continue
#
#     with open(BUFFER_FILE, 'r') as buffer_file:
#         client_file_name = buffer_file.readlines(1)[0].strip("\n")
#         client_file_text = ""
#         for line in buffer_file:
#             client_file_text += line
#         print(f"Text from the server buffer:\n{client_file_text}")
#         with open(client_file_name, 'w') as client_file:
#             client_file.write(client_file_text)
#
#     os.remove(LOCK_FILE)
#

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


        os.remove(LOCK_FILE)
        print(f"Odpowiedź została wysłana do klienta w pliku {client_response_file}.")

        time.sleep(1)


if __name__ == "__main__":
    print("Serwer uruchomiony. Oczekiwanie na wiadomości...")
    server_loop()
