import re
from collections import Counter


def parse_record(record: str):
    record = record.strip("#")
    record = record.strip("\n")
    record = re.split(' @ |,|:|x', record)
    record = [int(val) for val in record]
    return record[1:5]


def get_full_points_list(x, y, w, h):
    result = []
    x_max = x+w
    y_max = y+h

    for i in range(x, x_max):
        for j in range(y, y_max):
            result.append((i, j))
    return result


with open('day3_input.txt') as file:
    data = file.readlines()

records = [parse_record(line) for line in data]

list_of_point_lists = [get_full_points_list(*record) for record in records]

c = Counter()
for point_list in list_of_point_lists:
    for point in point_list:
        c.update([point])

p = [v for k, v in c.items() if v > 1]
print(len(p))


def calculate_list_overlap(a, b):
    d = Counter()
    d.update(a)
    d.update(b)

    p = [v for k, v in d.items() if v > 1]
    return len(p)


for idx, point_list_a in enumerate(list_of_point_lists):
    len_list = []
    for point_list_b in list_of_point_lists:
        if point_list_a == point_list_b:
            len_list.append(0)
            continue
        p = calculate_list_overlap(point_list_a, point_list_b)
        len_list.append(p)
    if sum(len_list) == 0:
        print(idx+1)
