class NumberProcessor:
    """Process number deduplication"""
    
    def remove_duplicates_right_to_left(self, n: int) -> int:
        """
        Retain the first occurrence of digits from right to left, removing duplicate digits.
        
        Args:
            n: Input positive integer (1 ≤ n ≤ 10^8), last digit is not 0
            
        Returns:
            int: Deduplicated number
        """
        # Convert number to string and reverse (process from right to left)
        num_str = str(n)[::-1]
        
        # Use set to record seen digits
        seen = set()
        result = []
        
        # Traverse the reversed string from left to right (equivalent to right to left of original number)
        for digit in num_str:
            if digit not in seen:
                seen.add(digit)
                result.append(digit)
        
        # Reverse the result back and convert to integer
        return int(''.join(result))


def main():
    # Read input
    n = int(input().strip())
    
    # Process number
    processor = NumberProcessor()
    result = processor.remove_duplicates_right_to_left(n)
    
    # Output result
    print(result)


if __name__ == "__main__":
    main() 