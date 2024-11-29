import os
import sysv_ipc

INPUT_QUEUE_KEY = 12345
OUTPUT_QUEUE_KEY = 56789

def main():
    input_queue = sysv_ipc.MessageQueue(INPUT_QUEUE_KEY)
    output_queue = sysv_ipc.MessageQueue(OUTPUT_QUEUE_KEY)
    client_pid = os.getpid()
    word = "car"
    for _ in range(5):
        input_queue.send(word.encode('utf-8'), type=client_pid)
        if word == "stop":
            print("Serwer został zatrzymany. Dalsze zapytania nie będą obsługiwane.")
            break
        message, _ = output_queue.receive(type=client_pid)
        response = message.decode('utf-8')
        print(f"Odpowiedź serwera: {response}")

if __name__ == "__main__":
    main()
