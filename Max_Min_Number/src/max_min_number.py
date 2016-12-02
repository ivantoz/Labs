def find_max_min(values):
    min = values[0]
    for elm in values[1:]:
        if elm < min:
            min = elm
    max = values[0]
    for elm in values[1:]:
        if elm > max:
            max = elm

    res = set()

    res.add(min)
    res.add(max)
    return sorted(list(res))


