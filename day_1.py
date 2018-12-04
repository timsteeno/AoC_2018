from itertools import cycle

with open('day1_input.txt') as file:
    freq_changes = file.read().splitlines()

freq_changes = [int(val) for val in freq_changes]

print("A1: {}".format(sum(freq_changes)))


def find_repeat(data):
    store = 0
    freq = [0]
    match = False
    gen_data = cycle(data)

    while not match:
        val = next(gen_data)
        store += val
        if store in freq:
            match = True
        freq.append(store)

    return store


f = find_repeat(freq_changes)

print("A2: {}".format(f))
