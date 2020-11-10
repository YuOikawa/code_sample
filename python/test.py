test = {"ichi": 1,"ni": 2,"san": 3}
sample = {"ichi": 4,"ni": 5,"san": 6}
sample2 = {"ichi": 1,"ni": 11,"san": 12}

print(test)

ultra = []

ultra.append(test)
ultra.append(sample)
ultra.append(sample2)
ultra.append(sample2)

print test["ichi"] in map(lambda x: x["ichi"], ultra)

def remove_duplicate(lst):
    ret_lst = []
    for d in lst:
        if d not in ret_lst:
            ret_lst.append(d)
    return ret_lst

print remove_duplicate(ultra)

tanoshi = {"a": {"ichi": 1,"ni": 2,"san": 3}, "b":{"ichi": 1,"ni": 2,"san": 3}}
print tanoshi

print "a" in tanoshi
