def encrypt(s: str) -> str:
    encrypted = []
    for char in s:
        if char.isalpha():
            if char.islower():
                encrypted.append(chr((ord(char) - ord('a') + 1) % 26 + ord('A')))
            else:
                encrypted.append(chr((ord(char) - ord('A') + 1) % 26 + ord('a')))
        elif char.isdigit():
            encrypted.append(str((int(char) + 1) % 10))
    return ''.join(encrypted)

def decrypt(t: str) -> str:
    decrypted = []
    for char in t:
        if char.isalpha():
            if char.islower():
                decrypted.append(chr((ord(char) - ord('a') - 1) % 26 + ord('A')))
            else:
                decrypted.append(chr((ord(char) - ord('A') - 1) % 26 + ord('a')))
        elif char.isdigit():
            decrypted.append(str((int(char) - 1) % 10))
    return ''.join(decrypted)

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    s = data[0].strip()
    t = data[1].strip()
    
    encrypted_s = encrypt(s)
    decrypted_t = decrypt(t)
    
    print(encrypted_s)
    print(decrypted_t)

if __name__ == "__main__":
    main()

