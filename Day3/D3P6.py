def smallest_not_in_list(list):
    sort(list)
    if list[0] != 0:
        return 0
    for i = 1 to list.last:
        if list[i] != list[i-1] + 1:
            return list[i-1] + 1
    if list[list.last] == 2^64 - 1:
        assert ("No gaps")
    return list[list.last] + 1
