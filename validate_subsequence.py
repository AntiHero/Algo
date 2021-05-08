array = [5, 1, 22, 25, 6, -1, 8, 10]
subseq = [1, 6, -1, 10]

# O(n) time | O(1) space


def validateSequence1(array, subseq):
    counter = 0
    for i in range(len(array)):
        if array[i] == subseq[counter]:
            counter += 1
            if counter == len(subseq):
                return True

    return False


print('validateSequence1', validateSequence1(array, subseq))

# O(n) time | O(1) space


def validateSequence2(array, subseq):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(subseq):
        if array[arrIdx] == subseq[seqIdx]:
            seqIdx += 1
        arrIdx += 1

    return seqIdx == len(subseq)


print('validateSequence2', validateSequence2(array, subseq))
