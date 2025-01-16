def min_servers_required(tasks: list) -> int:
    events = []
    for start, end, parallel in tasks:
        events.append((start, parallel))
        events.append((end, -parallel))

    events.sort()
    # print(events)
    current_servers = 0
    max_servers = 0
    for _, parallel in events:
        current_servers += parallel
        max_servers = max(max_servers, current_servers)
    return max_servers

def main():
    num_tasks = int(input().strip())
    tasks = []
    for _ in range(num_tasks):
        tasks.append(list(map(int, input().strip().split())))

    print(min_servers_required(tasks))

if __name__ == "__main__":
    tasks = [
        [1, 2, 1],
        [2, 3, 3],
        [3, 4, 1],
        [4, 5, 1]
    ]
    print(min_servers_required(tasks))
