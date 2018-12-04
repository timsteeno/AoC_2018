from collections import Counter


def get_checksum(list_of_words):
    """
    Given a list of words, calculate a sum total T2 of all exact-twos
    Given a list of words, calculate a sum total T3 of all exact-threes
    Return T2 * T3
    """
    twos_sum = get_total_exact_n(list_of_words, 2)
    threes_sum = get_total_exact_n(list_of_words, 3)
    return twos_sum * threes_sum


def get_total_exact_n(list_of_words, n):
    """Given a list of words, get a 0/1 value for each word:
           0 if there are no letters repeated exactly twice
           1 if one or more letters are repeated exactly twice"""
    store = []
    for word in list_of_words:
        dict_with_n = {k: v for (k, v) in Counter(word).items() if v == n}
        if len(dict_with_n) > 0:
            store.append(1)
        else:
            store.append(0)
    return sum(store)


def compare_strings(str1, str2):
    """Returns the number of exact position differences between str1 and str2."""
    count = 0
    for idx, val in enumerate(str1):
        if str2[idx] != val:
            count += 1
    return count


def compare_string_list(str_list):
    comparisons = {}
    for str1 in str_list:
        for str2 in str_list:
            comparisons[(str1, str2)] = compare_strings(str1, str2)
    return comparisons


def compare_string_text(str1, str2):
    """Returns the letters that match between str1 and str2."""
    text = ""
    for idx, val in enumerate(str1):
        if str2[idx] == val:
            text += val
    return text


with open('day2_input.txt') as file:
    data = file.readlines()

chksum = get_checksum(data)

print("A: {}".format(chksum))

compares = compare_string_list(data)

package_match = [(k1, k2) for (k1, k2), v in compares.items() if v == 1]
print("B: {}".format(compare_string_text(*package_match[0])))
