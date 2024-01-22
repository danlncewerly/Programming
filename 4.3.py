def func(strings):
    new_s = {}
    for s in strings:
        key = ''.join(sorted(s))
        if len(s) in new_s:
            if key in new_s[len(s)]:
                new_s[len(s)][key].append(s)
            else:
                new_s[len(s)][key] = [s]
        else:
            new_s[len(s)] = {key: [s]}

    result = []
    for k in sorted(new_s.keys()):
        for key in new_s[k]:
            result.append(new_s[k][key])
    return result

if __name__=='__main__':
    input1 = ["qwe", "ewq", "asd", "dsa", "dsas", "qwee", "zxc", "cxz", "xxz", "z", "s", "qweasdzxc", "zzxc"]
    print(func(input1))
    input2 = ["a", "a", ""]
    print(func(input2))
