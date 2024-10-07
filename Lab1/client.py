import time

num = str(input("Podaj pojedynczą liczbę całkowitą\n"))

with open("data.txt", 'w') as plik:
    plik.write(num)

time.sleep(3)

with open("results.txt", "r") as plik2:
    result = plik2.read()
    print(result)