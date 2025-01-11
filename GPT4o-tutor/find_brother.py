def find_brothers(querys: list[str], target: str, k: int) -> tuple:
    brothers = [query for query in querys if is_brother(query, target)]
    brothers.sort()
    count = len(brothers)
    kth_brother = brothers[k - 1] if count >= k else ""
    return count, kth_brother


def is_brother(query: str, target: str) -> bool:
    return sorted(query) == sorted(target) and query != target


if __name__ == "__main__":
    import sys
    input_lines = input().strip().split()
    query_num = int(input_lines[0])
    querys = input_lines[1:query_num + 1]
    target = input_lines[query_num + 1]
    k = int(input_lines[-1])

    count, result = find_brothers(querys, target, k)
    print(count)
    if result:
        print(result)
