import os

FIFO_SERVER = "/tmp/server_fifo"
FIFO_CLIENT = input("Input client fifo path:\n")

if not os.path.exists(FIFO_CLIENT):
    os.mkfifo(FIFO_CLIENT)

client_id = int(input("Input ID: "))

path_bytes = FIFO_CLIENT.encode('utf-8')
path_bytes = path_bytes.ljust(100, b'\x00')

message = (len(path_bytes) + 4).to_bytes(4, 'little') + client_id.to_bytes(4, 'little') + path_bytes

with open(FIFO_SERVER, "wb") as server_fifo:
    server_fifo.write(message)

with open(FIFO_CLIENT, "rb") as client_fifo:
    response_length = int.from_bytes(client_fifo.read(4), 'little')
    response = client_fifo.read(response_length).decode('utf-8')
    print("Response from server:", response)
