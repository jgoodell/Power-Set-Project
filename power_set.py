def power_set(set):
    power_set = [[]]
    new_sets = [] # holds the new sets
    for item in set:
        for each in power_set:
            new_sets.append(each + [item])
        power_set += new_sets # add new sets outside power_set loop
        new_sets = []
    return power_set
