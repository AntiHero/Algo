array = [5, 1, 22, 25, 6, -1, 8, 10]
subseq = [1, 6, -1, 10]


# O(n) time | O(1) space
def validate_sequence1(arr, seq):
    counter = 0
    for i in range(len(arr)):
        if arr[i] == seq[counter]:
            counter += 1
            if counter == len(seq):
                return True

    return False


print('validate_sequence1', validate_sequence1(array, subseq))


# O(n) time | O(1) space
def validate_sequence2(arr, seq):
    arr_idx = 0
    seq_idx = 0
    while arr_idx < len(array) and seq_idx < len(seq):
        if arr[arr_idx] == seq[seq_idx]:
            seq_idx += 1
        arr_idx += 1

    return seq_idx == len(seq)


print('validate_sequence2', validate_sequence2(array, subseq))
