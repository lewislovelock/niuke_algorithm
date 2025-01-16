def reverse_number(n: int) -> int:
    """
    将数字翻转
    
    Args:
        n: 输入的正整数
        
    Returns:
        翻转后的数字
        
    Example:
        >>> reverse_number(12)
        21
    """
    return int(str(n)[::-1])

def solve() -> None:
    """
    主要解决函数
    数据流: 输入 -> 翻转 -> 求和 -> 输出
    """
    # 1. 输入处理
    a = int(input().strip())
    
    # 2. 数据转换：原数字 -> 翻转数字
    b = reverse_number(a)
    
    # 3. 计算结果
    result = a + b
    
    # 4. 输出结果
    print(result)

# ACM模式入口
if __name__ == "__main__":
    solve()