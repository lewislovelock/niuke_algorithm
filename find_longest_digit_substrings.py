import re
import sys

def find_longest_digit_substrings(s: str) -> str:
    # 使用正则表达式提取所有数字子串
    digit_substrings = re.findall(r'\d+', s)
    
    # 找出最长的数字子串长度
    max_length = max(len(substring) for substring in digit_substrings)
    
    # 找出所有最长的数字子串
    longest_substrings = [substring for substring in digit_substrings if len(substring) == max_length]
    
    # 输出结果
    return ','.join(longest_substrings) + f',{max_length}'

def main():
    # 从标准输入读取数据
    inputs = sys.stdin.read().strip().split()
    
    # 处理每个输入
    for input_str in inputs:
        result = find_longest_digit_substrings(input_str)
        print(result)

if __name__ == "__main__":
    main()