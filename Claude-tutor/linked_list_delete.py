class ListNode:
    def __init__(self, val: int = 0, next = None):
        self.val = val
        self.next = next


def build_linked_list(head_val: int, n: int, input_data: list[str]) -> ListNode:
    head = ListNode(head_val)
    value_to_node = {head_val: head}
    idx = 0
    for _ in range(n - 1):
        a, b = int(input_data[idx]), int(input_data[idx + 1])
        idx += 2
        new_node = ListNode(a)
        b_node = value_to_node[b]
        new_node.next = b_node.next
        b_node.next = new_node
        value_to_node[a] = new_node
    return head


def delete_node(head: ListNode, k: int) -> ListNode:
    dummy = ListNode(0, head)
    prev, curr = dummy, head

    while curr:
        if curr.val == k:
            prev.next = curr.next
            break
        prev, curr = curr, curr.next
    return dummy.next


def print_linked_list(head: ListNode) -> None:
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    print(" ".join(map(str, result)))


def main():
    input_data = input().strip().split()
    n = int(input_data[0])
    head_val = int(input_data[1])
    k = int(input_data[-1])

    linked_list = build_linked_list(head_val, n, input_data[2:-1])
    linked_list = delete_node(linked_list, k)
    print_linked_list(linked_list)


if __name__ == "__main__":
    main()