def reformat(s):
    flag = True
    res = []
    i = 7
    while flag:
        if s[i].isalpha():
            res.append(s[i])
        elif s[i] == ",":
            flag = False
            break
        i += 1
    return "".join(res)
