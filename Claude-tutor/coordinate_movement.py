from typing import Tuple, Dict
from dataclasses import dataclass


@dataclass
class Position:
    """Represents a position in 2D grid"""
    x: int = 0
    y: int = 0


class CoordinateMovement:
    """Handles the movement of a character on a 2D grid based on instructions"""
    
    def __init__(self):
        # Direction mapping: how each direction affects coordinates
        self.direction_map: Dict[str, Tuple[int, int]] = {
            'A': (-1, 0),  # Left
            'D': (1, 0),   # Right
            'W': (0, 1),   # Up
            'S': (0, -1)   # Down
        }
        self.position = Position()

    def is_valid_instruction(self, instruction: str) -> bool:
        """
        Validates if the instruction follows the correct format.
        
        Args:
            instruction: A string containing a single movement instruction
            
        Returns:
            bool: True if instruction is valid, False otherwise
        """
        if len(instruction) < 3 or not instruction.endswith(';'):
            return False
            
        direction = instruction[0]
        if direction not in self.direction_map:
            return False
            
        # Extract the number part (excluding first char and last semicolon)
        number_part = instruction[1:-1]
        if not number_part.isdigit():
            return False
            
        number = int(number_part)
        return 1 <= number <= 99

    def process_instruction(self, instruction: str) -> None:
        """
        Processes a single valid instruction and updates the position.
        
        Args:
            instruction: A string containing a single movement instruction
        """
        if not self.is_valid_instruction(instruction):
            return
            
        direction = instruction[0]
        steps = int(instruction[1:-1])
        
        dx, dy = self.direction_map[direction]
        self.position.x += dx * steps
        self.position.y += dy * steps

    def process_instructions(self, instructions: str) -> str:
        """
        Processes a sequence of instructions and returns final position.
        
        Args:
            instructions: A string containing multiple movement instructions
            
        Returns:
            str: Final position in format "x,y"
        """
        # Reset position
        self.position = Position()
        
        # Split instructions by semicolon and filter out empty ones
        # A10;S20;W10;D30;X;A1A;B10A11;;A10;
        instruction_list = [inst + ';' for inst in instructions.split(';')[:-1]]
        
        # Process each instruction
        for instruction in instruction_list:
            self.process_instruction(instruction)
            
        return f"{self.position.x},{self.position.y}"


def main():
    # Read input
    instructions = input().strip()
    
    # Process instructions and get result
    movement = CoordinateMovement()
    result = movement.process_instructions(instructions)
    
    # Output result
    print(result)


if __name__ == "__main__":
    main() 