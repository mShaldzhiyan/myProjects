def lengthOfLongestSubstring(s: str) -> int:
    substr = ''
    count = 0
    subcount = 0
    if len(s) < 1:
        return 0
    for a in s:
        if a not in substr:
            substr += a
            subcount += 1
            if subcount > count:
                count = subcount
        else:
            if subcount > count:
                count = subcount
            i = substr.index(a) + 1
            substr = substr[i:]
            substr += a
            subcount = len(substr)
        if subcount > count:
            count = subcount
    return count

print(lengthOfLongestSubstring("dvdf"))