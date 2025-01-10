from typing import List, Tuple
from dataclasses import dataclass


@dataclass
class Item:
    """Class to represent a shopping item"""
    price: int
    importance: int
    main_item_id: int
    item_id: int


def solve_shopping(budget: int, items: List[Item]) -> int:
    """
    Calculate the maximum satisfaction value within the budget constraint.
    
    Args:
        budget: Total available budget
        items: List of items with their properties
        
    Returns:
        int: Maximum satisfaction value achievable
    """
    # Group items by main items and their attachments
    main_items = {}
    for item in items:
        if item.main_item_id == 0:  # This is a main item
            main_items[item.item_id] = {
                'main': item,
                'attachments': []
            }
    
    # Add attachments to their main items
    for item in items:
        if item.main_item_id > 0:  # This is an attachment
            if item.main_item_id in main_items:
                main_items[item.main_item_id]['attachments'].append(item)
    
    # Create dp array
    dp = [0] * (budget + 1)
    
    # For each main item and its possible attachment combinations
    for main_id, item_group in main_items.items():
        main = item_group['main']
        attachments = item_group['attachments']
        
        # Create all possible combinations
        for money in range(budget, -1, -1):
            # Try main item alone
            if money >= main.price:
                satisfaction = main.price * main.importance
                dp[money] = max(dp[money], dp[money - main.price] + satisfaction)
            
            # Try main item with first attachment
            if len(attachments) >= 1 and money >= main.price + attachments[0].price:
                satisfaction = (main.price * main.importance + 
                              attachments[0].price * attachments[0].importance)
                dp[money] = max(dp[money], 
                              dp[money - main.price - attachments[0].price] + satisfaction)
            
            # Try main item with second attachment
            if len(attachments) >= 2 and money >= main.price + attachments[1].price:
                satisfaction = (main.price * main.importance + 
                              attachments[1].price * attachments[1].importance)
                dp[money] = max(dp[money], 
                              dp[money - main.price - attachments[1].price] + satisfaction)
            
            # Try main item with both attachments
            if len(attachments) >= 2 and money >= main.price + attachments[0].price + attachments[1].price:
                satisfaction = (main.price * main.importance + 
                              attachments[0].price * attachments[0].importance +
                              attachments[1].price * attachments[1].importance)
                dp[money] = max(dp[money], 
                              dp[money - main.price - attachments[0].price - attachments[1].price] + satisfaction)
    
    return dp[budget]


def main():
    # Read input
    budget, n = map(int, input().split())
    
    # Read items
    items = []
    for i in range(n):
        price, importance, main_item_id = map(int, input().split())
        items.append(Item(price, importance, main_item_id, i + 1))
    
    # Calculate and output result
    result = solve_shopping(budget, items)
    print(result)


if __name__ == "__main__":
    main() 