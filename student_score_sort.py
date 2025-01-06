"""
Sort students by their scores while maintaining stable order for equal scores.

This module provides a solution for sorting student information (name and score)
based on their scores, either in ascending or descending order.
"""
from typing import List, Tuple


def sort_students(students: List[Tuple[str, int]], ascending: bool) -> List[Tuple[str, int]]:
    """
    Sort students by their scores while maintaining original order for equal scores.
    
    Args:
        students: List of (name, score) tuples
        ascending: If True, sort from low to high; if False, sort from high to low
    
    Returns:
        List of (name, score) tuples sorted according to the specified order
    
    Examples:
        >>> sort_students([("jack", 70), ("peter", 96), ("Tom", 70)], False)
        [("peter", 96), ("jack", 70), ("Tom", 70)]
    """
    # Use enumerate to maintain original position for stable sort
    indexed_students = list(enumerate(students))
    
    # Sort by score and original position
    # For equal scores, earlier positions come first
    indexed_students.sort(key=lambda x: (x[1][1], x[0]) if ascending else (-x[1][1], x[0]))
    
    # Return only the student information without indices
    return [student for _, student in indexed_students]


def main():
    """Main function to handle ACM-style input/output."""
    try:
        # Read number of students
        n = int(input().strip())
        if not (1 <= n <= 200):
            raise ValueError("Number of students must be between 1 and 200")
        
        # Read sort order (0: descending, 1: ascending)
        sort_order = int(input().strip())
        if sort_order not in (0, 1):
            raise ValueError("Sort order must be 0 or 1")
        
        # Read student information
        students: List[Tuple[str, int]] = []
        for _ in range(n):
            name, score = input().strip().split()
            score = int(score)
            students.append((name, score))
        
        # Sort and print results
        sorted_students = sort_students(students, ascending=(sort_order == 1))
        for name, score in sorted_students:
            print(f"{name} {score}")
            
    except ValueError as e:
        print(f"Invalid input: {e}")
    except EOFError:
        pass


if __name__ == "__main__":
    main() 