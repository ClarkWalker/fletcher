import time

def make_some_cpu_heat_to_turn_on_fans():
    i = 0
    while i <= 7_000_000:
        time.sleep(1)
        print(i)
        i += 1


make_some_cpu_heat_to_turn_on_fans()
