from typing import List

def process_numbers(numbers: List[int]) -> List[int]:
    """
    处理输入的数字列表：去重并排序
    
    Args:
        numbers (List[int]): 输入的整数列表，范围在1到500之间
        
    Returns:
        List[int]: 去重并排序后的整数列表
        
    Time Complexity: O(nlogn)
    Space Complexity: O(n)
    """
    # 使用集合去重，然后排序
    return sorted(set(numbers))

def main() -> None:
    try:
        # 读取数字个数
        n = int(input().strip())
        
        # 输入验证
        if not 1 <= n <= 1000:
            raise ValueError("n must be between 1 and 1000")
        
        # 读取n个数字
        numbers: List[int] = []
        for _ in range(n):
            num = int(input().strip())
            # 输入验证
            if not 1 <= num <= 500:
                raise ValueError("Each number must be between 1 and 500")
            numbers.append(num)
        
        # 处理数字并输出
        result = process_numbers(numbers)
        for num in result:
            print(num)
            
    except ValueError as e:
        # 在实际提交时，可以去掉错误信息的打印
        print(f"Error: {e}")
    except EOFError:
        pass

if __name__ == "__main__":
    main() 