#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set()
    for m in set_2:
        for i in set_1:
            if i == m:
                new_set.add(i)
    new_set_combined = set_1 | set_2
    last_set = new_set_combined - new_set
    return last_set
