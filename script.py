import time

my_time = int(input("Countdown for how many seconds?: "))
my_time += 1

for i in reversed(range(0, my_time)):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600)

    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Times UP!")