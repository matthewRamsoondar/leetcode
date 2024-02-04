def authEvents(events):
    # Write your code here
    p, M = 131, 10**9 + 7

    def hash_string(s):
        _sum, n = 0, len(s)
        for i in range(n):
            _sum += ord(s[i]) * (p ** (n - i - 1))

        return _sum % M

    res = []

    cur_password, cur_hash = "", 0
    memo = set()
    for event in events:
        if event[0] == "setPassword":
            cur_password = event[1]
            memo = set()
            cur_hash = hash_string(cur_password)
            memo.add(cur_hash)
        else:
            _input = int(event[1])

            # print(_input, memo, _input in memo)
            if _input in memo:
                res.append(1)
                continue

            n = len(res)
            for i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890":
                h = hash_string(cur_password + i)
                memo.add(h)
                if _input == h:
                    res.append(1)
                    break

            if n == len(res):
                res.append(0)
    return res


events = [
    ["setPassword", "000A"],
    ["authorize", "108738450"],
    ["authorize", "108738449"],
    ["authorize", "244736787"],
]

print(authEvents(events))
