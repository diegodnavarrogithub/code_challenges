def longest_common_prefix(strs):
    if len(strs) < 2:
        return strs[0]

    ref = strs[0]

    for s in strs:
        if len(s) < len(ref):
            ref = s

    index = 0
    ans = ""
    while index <= len(ref):
        cur_pref = ref[:index]
        for s in strs:
            if not s.startswith(cur_pref):
                return ans
        ans = cur_pref
        index += 1
    return ans
