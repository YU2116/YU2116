import time


def pascal(n):
    if n == 0:
        return [1]
    
    prev_row = pascal(n - 1)
    
    curr_row = [1]
    for i in range(len(prev_row) - 1):
        curr_row.append(prev_row[i] + prev_row[i + 1])
    curr_row.append(1)
    
    return curr_row


def pascal_iter(n):
    row = [1]
    for _ in range(n):
        next_row = [1]
        for i in range(len(row) - 1):
            next_row.append(row[i] + row[i + 1])
        next_row.append(1)
        row = next_row
    return row


def test_pascal():
    test_cases = [0, 1, 3, 4]
    expected_results = [
        [1],
        [1, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]
    ]
    
    print("--- 开始检查递归版 ---")
    for n, expected in zip(test_cases, expected_results):
        result = pascal(n)
        status = "通过" if result == expected else "不通过"
        print(f"n={n}: 结果={result}, 预期={expected} -> {status}")
        
    print("\n--- 开始检查迭代版 ---")
    for n, expected in zip(test_cases, expected_results):
        result = pascal_iter(n)
        status = "通过" if result == expected else "不通过"
        print(f"n={n}: 结果={result}, 预期={expected} -> {status}")


def speed_compare():
    print("\n--- 速度对比 ---")
    n = 20 
    
    start_time = time.time()
    pascal(n)
    rec_time = time.time() - start_time
    print(f"递归版 pascal({n}) 耗时: {rec_time:.6f} 秒")
    
    start_time = time.time()
    pascal_iter(n)
    iter_time = time.time() - start_time
    print(f"迭代版 pascal_iter({n}) 耗时: {iter_time:.6f} 秒")


if __name__ == "__main__":
    test_pascal()
    speed_compare()
