from collections import Counter
from typing import Dict


class StringProcessor:
    """Process string by removing least frequent characters"""
    
    def remove_least_frequent(self, s: str) -> str:
        """
        Remove characters that appear least frequently in the string.
        If multiple characters have the same minimum frequency, remove all of them.
        
        Args:
            s: Input string containing only lowercase letters
            
        Returns:
            str: String after removing least frequent characters
        """
        # Count character frequencies using Counter
        char_count = Counter(s)
        
        # Find minimum frequency
        min_count = min(char_count.values())
        
        # Find all characters with minimum frequency
        chars_to_remove = {
            char for char, count in char_count.items()
            if count == min_count
        }
        
        # Build result string while maintaining original order
        result = ''.join(
            char for char in s
            if char not in chars_to_remove
        )
        
        return result


def main():
    # Read input
    s = input().strip()
    
    # Process string
    processor = StringProcessor()
    result = processor.remove_least_frequent(s)
    
    # Output result
    print(result)


if __name__ == "__main__":
    main() 