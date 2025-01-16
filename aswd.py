def aswd(s: str) -> int:
    count = {"A": 0, "S": 0, "D": 0, "W": 0}
    for c in s:
        count[c] += 1
    
    max_count = max(count.values())
    min_count = min(count.values())
    return max_count - min_count

if __name__ == "__main__":
    s = input().strip()
    print(aswd(s))