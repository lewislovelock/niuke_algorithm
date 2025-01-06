"""
Count unique ASCII characters in a string.

This module provides a solution for counting the number of unique ASCII characters
in a given string, where the characters are in the visible ASCII range (33-126).
"""
from typing import Set


def count_unique_chars(s: str) -> int:
    """
    Count the number of unique ASCII characters in the input string.
    
    Args:
        s: Input string with length between 1 and 500, containing only visible ASCII chars
           (ASCII codes 33-126)
    
    Returns:
        int: Number of unique characters in the string
    
    Examples:
        >>> count_unique_chars("hello")
        4  # unique chars are 'h', 'e', 'l', 'o'
        >>> count_unique_chars("aaa")
        1  # only one unique char 'a'
    """
    # Convert string to set to get unique characters
    unique_chars: Set[str] = set(s)
    return len(unique_chars)


def main():
    """Main function to handle ACM-style input/output."""
    try:
        # Read one line of input
        s = input().strip()
        
        # Validate input length
        if not (1 <= len(s) <= 500):
            raise ValueError("Input string length must be between 1 and 500")
            
        # Get and print result
        result = count_unique_chars(s)
        print(result)
        
    except EOFError:
        pass
    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main() 