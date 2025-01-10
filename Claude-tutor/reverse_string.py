class StringReverser:
    """Process string reversal"""
    
    def reverse_string(self, s: str) -> str:
        """
        Reverse the input string.
        
        Args:
            s: Input string containing only lowercase letters
            
        Returns:
            str: Reversed string
        """
        return s[::-1]


def main():
    # Read input
    s = input().strip()
    
    # Reverse string
    reverser = StringReverser()
    result = reverser.reverse_string(s)
    
    # Output result
    print(result)


if __name__ == "__main__":
    main() 