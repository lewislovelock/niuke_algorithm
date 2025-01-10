def sort_string(s: str) -> str:
    letters =[c for c in s if c.isalpha()]
    letters.sort(key=lambda x: x.lower())
    
    letter_iter = iter(letters)
    result = []
    result = "".join(next(letter_iter) if c.isalpha() else c for c in s)
    return result
        
def main():
    import sys
    input = sys.stdin.readline
    s = input().strip()
    print(sort_string(s))

if __name__ == '__main__':
    main()