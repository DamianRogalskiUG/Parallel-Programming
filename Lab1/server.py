import time

running = True

while running:
    time.sleep(1)
    with open("data.txt", 'r') as plik:
        num = int(plik.read())
        result = str(num * num)
    time.sleep(1)
    with open("results.txt", 'w') as plik2:
        plik2.write(result)

