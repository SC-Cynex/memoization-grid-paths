def count_paths(m, n, memo=None):
    if memo is None:
        memo = {}

    if (m, n) in memo:
        return memo[(m, n)]

    if m == 1 or n == 1:
        return 1

    memo[(m, n)] = count_paths(m - 1, n, memo) + count_paths(m, n - 1, memo)
    return memo[(m, n)]

def count_paths_no_cache(m, n):
    if m == 1 or n == 1:
        return 1
    return count_paths_no_cache(m - 1, n) + count_paths_no_cache(m, n - 1)
