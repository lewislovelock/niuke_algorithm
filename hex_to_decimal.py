def hex_to_decimal(hex_str: str) -> int:
    """
    将十六进制字符串转换为十进制整数
    
    Args:
        hex_str (str): 以'0x'开头的十六进制字符串
        
    Returns:
        int: 转换后的十进制整数
        
    Raises:
        ValueError: 当输入字符串格式不正确时
    """
    if not hex_str.startswith("0x"):
        raise ValueError("Input string must start with '0x'")
    
    # 去掉'0x'前缀
    hex_str = hex_str[2:]
    
    # 创建十六进制字符到数值的映射
    hex_map = {str(i): i for i in range(10)}
    hex_map.update({
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
        'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15  # 支持小写字母
    })
    
    result = 0
    for char in hex_str:
        if char not in hex_map:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        result = result * 16 + hex_map[char]
    
    return result

def main():
    """
    牛客网 ACM 模式主函数
    处理输入输出
    """
    try:
        # 牛客网中，输入是一行一个十六进制数
        while True:
            try:
                hex_str = input().strip()  # 读取一行输入
                if not hex_str:  # 处理输入结束的情况
                    break
                
                # 转换并输出结果
                result = hex_to_decimal(hex_str)
                print(result)
                
            except ValueError as e:
                # 在实际提交时，可能需要去掉错误信息的打印
                print(f"Error: {e}")
            except EOFError:
                break
                
    except EOFError:
        pass

if __name__ == "__main__":
    main()