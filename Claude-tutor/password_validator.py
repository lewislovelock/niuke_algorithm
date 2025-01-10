from typing import Set

class PasswordValidator:
    """Password validator that checks if a password meets specific requirements."""

    def __init__(self):
        self.MIN_TYPES = 3

    def has_required_char_types(self, password: str) -> bool:
        """
        Check if password contains at least 3 types of characters.
        
        Args:
            password: The password string to validate
            
        Returns:
            bool: True if password contains at least 3 types of characters
        """
        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False
        
        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
            elif 33 <= ord(char) <= 126:
                has_special = True
                
        return sum([has_upper, has_lower, has_digit, has_special]) >= self.MIN_TYPES

    def has_repeating_substring(self, password: str) -> bool:
        """
        Check if password contains two independent repeating substrings of length > 2.
        Independent means the substrings don't overlap.
        
        Args:
            password: The password string to validate
            
        Returns:
            bool: True if independent repeating substrings found
        """
        n = len(password)
        for length in range(3, n // 2 + 1):
            for i in range(n - length * 2 + 1):
                current = password[i:i + length]
                remaining = password[i + length:]
                if current in remaining:
                    return True
        return False

    def is_valid_password(self, password: str) -> bool:
        """
        Validate if the password meets all requirements.
        
        Args:
            password: The password string to validate
            
        Returns:
            bool: True if password is valid
        """
        if not self.has_required_char_types(password):
            return False
        if self.has_repeating_substring(password):
            return False
        return True


def main():
    validator = PasswordValidator()
    
    try:
        while True:
            password = input().strip()
            result = validator.is_valid_password(password)
            print("OK" if result else "NG")
    except EOFError:
        pass


if __name__ == "__main__":
    main() 