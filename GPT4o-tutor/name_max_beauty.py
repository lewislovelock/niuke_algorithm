def cal_max_beauty(s: str) -> int:
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    sorted_frequency = sorted(frequency.values(), reverse=True)

    max_beauty = 0
    beauty_value = 26
    for freq in sorted_frequency:
        max_beauty += freq * beauty_value
        beauty_value -= 1
    return max_beauty

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    n = int(data[0].strip())

    for i in range(1, n + 1):
        s = data[i].strip()
        print(cal_max_beauty(s))


if __name__ == "__main__":
    main()