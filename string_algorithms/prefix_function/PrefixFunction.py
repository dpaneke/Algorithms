def prefix_function(s: str) -> list[int]:
    """calculates len of greatest border of string s for each position i"""
    prefix_arr = [0] * len(s)
    def prefix_func_i(i):
        j = i - 1
        while j >= 0:
            k = prefix_arr[j]
            if s[k] == s[i]: return k + 1
            j = k - 1
        return 0
    for i in range(1, len(s)):
        prefix_arr[i] = prefix_func_i(i)
    return prefix_arr