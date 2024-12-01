import sysv_ipc
import time

INPUT_QUEUE_KEY = 12345
OUTPUT_QUEUE_KEY = 56789

DICTIONARY = {
    "hello": "cześć",
    "bye bye": "pa pa",
    "car": "samochód",
    "book": "książka"
}


def main():
    try:
        input_queue = sysv_ipc.MessageQueue(INPUT_QUEUE_KEY, sysv_ipc.IPC_CREX)
        output_queue = sysv_ipc.MessageQueue(OUTPUT_QUEUE_KEY, sysv_ipc.IPC_CREX)
        print("Server is running. Waiting for messages...")

        while True:
            message, client_pid = input_queue.receive(type=0)
            word = message.decode('utf-8')
            if word.lower() == "stop":
                print("Stop signal received.")
                break
            time.sleep(2)
            response = DICTIONARY.get(word.lower(), "Word unrecognized.")
            output_queue.send(response.encode('utf-8'), type=client_pid)

    finally:
        input_queue.remove()
        output_queue.remove()
        print("Server stopped, queues deleted.")


if __name__ == "__main__":
    main()
