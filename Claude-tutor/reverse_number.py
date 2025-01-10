class NumberReverser:
    """Process number reversal, preserving leading zeros"""
    
    def reverse_number(self, n: int) -> str:
        """
        Convert number to string and reverse, preserving leading zeros.
        
        Args:
            n: Input non-negative integer (0 ≤ n < 2^30)
            
        Returns:
            str: Reversed number string
        """
        # Convert number to string
        num_str = str(n)
        
        # Reverse string
        return num_str[::-1]


def main():
    # Read input
    n = int(input().strip())
    
    # Reverse number
    reverser = NumberReverser()
    result = reverser.reverse_number(n)
    
    # Output result
    print(result)


if __name__ == "__main__":
    main() 