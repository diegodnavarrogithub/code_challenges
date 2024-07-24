def valid_anagram(s: str, t: str):
    s = list(s)
    s.sort()
    t = list(t)
    t.sort()
    return s == t
