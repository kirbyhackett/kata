# Kata provided by CodeKata
# http://codekata.com/kata/kata02-karate-chop/


def main():
    # recursive function
    test_chop(recursive_chop)


def recursive_chop(num, arr):
    if len(arr) == 0 or (len(arr) == 1 and arr[0] != num):
        return -1

    position = round(len(arr) / 2)

    if arr[position] == num:
        return position
    elif arr[position] > num:
        return recursive_chop(num, arr[:position])
    elif arr[position] < num:
        val = recursive_chop(num, arr[position:])
        return -1 if val == -1 else position + val


def test_chop(chop):
    assert -1 == chop(3, [])
    assert -1 == chop(3, [1])
    assert 0 == chop(1, [1])
    #
    assert 0 == chop(1, [1, 3, 5])
    assert 1 == chop(3, [1, 3, 5])
    assert 2 == chop(5, [1, 3, 5])
    assert -1 == chop(0, [1, 3, 5])
    assert -1 == chop(2, [1, 3, 5])
    assert -1 == chop(4, [1, 3, 5])
    assert -1 == chop(6, [1, 3, 5])
    #
    assert 0 == chop(1, [1, 3, 5, 7])
    assert 1 == chop(3, [1, 3, 5, 7])
    assert 2 == chop(5, [1, 3, 5, 7])
    assert 3 == chop(7, [1, 3, 5, 7])
    assert -1 == chop(0, [1, 3, 5, 7])
    assert -1 == chop(2, [1, 3, 5, 7])
    assert -1 == chop(4, [1, 3, 5, 7])
    assert -1 == chop(6, [1, 3, 5, 7])
    assert -1 == chop(8, [1, 3, 5, 7])


main()
