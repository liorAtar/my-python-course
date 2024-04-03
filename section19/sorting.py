def bubble_sort(nlist: list) -> list:
    """
    Sorts a list using the Bubble Sort algorithm.

    Args:
        nlist: List of elements to be sorted.

    Returns:
        Sorted list.
    """
    nlist_length = len(nlist)
    for i in range(nlist_length):
        for j in range(0, nlist_length - i - 1):
            if nlist[j] > nlist[j + 1]:
                lower = nlist[j + 1]
                bigger = nlist[j]
                nlist[j] = lower
                nlist[j + 1] = bigger
    return nlist


def merge(rlist: list, llist: list) -> list:
    """
    Merges two sorted lists into a single sorted list.

    Args:
        rlist: Right list to be merged.
        llist: Left list to be merged.

    Returns:
        Merged and sorted list.
    """
    sorted_list = []
    left_idx, right_idx = 0, 0

    while left_idx < len(llist) and right_idx < len(rlist):
        if llist[left_idx] > rlist[right_idx]:
            sorted_list.append(rlist[right_idx])
            right_idx += 1
        elif llist[left_idx] < rlist[right_idx]:
            sorted_list.append(llist[left_idx])
            left_idx += 1

    sorted_list.extend(llist[left_idx:])
    sorted_list.extend(rlist[right_idx:])

    return sorted_list


def merge_sort(nlist: list) -> list:
    """
    Sorts a list using the Merge Sort algorithm.

    Args:
        nlist: List of elements to be sorted.

    Returns:
        Sorted list.
    """
    if len(nlist) <= 1:
        return nlist

    mid_idx = len(nlist) // 2
    right_list = nlist[:mid_idx]
    left_list = nlist[mid_idx:]

    right_list = merge_sort(right_list)
    left_list = merge_sort(left_list)

    return merge(right_list, left_list)


if __name__ == "__main__":
    num_list = [1, 34, 25, 12, 22, 11, 90]
    sorted_l = merge_sort(num_list)
    print("Array to sort:", num_list)
    print("Sorted array:", sorted_l)
