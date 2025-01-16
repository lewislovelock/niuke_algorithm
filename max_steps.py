def find_longest_path(n: int, heights: list[int]) -> int:
    """
    使用动态规划找出最长递增路径
    
    Args:
        n: 梅花桩的数量
        heights: 每个梅花桩的高度列表
    
    Returns:
        int: 最长可能的步数
    """
    # dp[i] 表示从位置i开始能走的最大步数
    dp = [1] * n  # 初始化为1，因为每个位置至少可以走1步
    
    # 从后往前遍历每个起点
    for i in range(n-1, -1, -1):
        # 遍历i后面的所有位置
        for j in range(i+1, n):
            # 如果可以从i走到j（严格递增）
            if heights[j] > heights[i]:
                # 更新dp[i]：从i到j的一步 + 从j开始能走的步数
                dp[i] = max(dp[i], dp[j] + 1)
    
    # 返回所有起点中的最大值
    return max(dp)

def main():
    # 读取梅花桩数量
    n = int(input().strip())
    # 读取每个梅花桩的高度
    heights = list(map(int, input().strip().split()))
    
    # 计算并输出结果
    result = find_longest_path(n, heights)
    print(result)

if __name__ == "__main__":
    main()