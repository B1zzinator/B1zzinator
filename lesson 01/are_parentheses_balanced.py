def get_longest_uniq_length(origin: str, /) -> int:
    """
    Возвращает длину самой длинной последовательности уникальных символов
    :param origin: исходная последовательность
    :type origin: str
    :return: длина самой длинной последовательности уникальных символов
    :rtype: int
    Примеры использования:
    >>> assert get_longest_uniq_length("abcdefg") == 7
    >>> assert get_longest_uniq_length("racecar") == 5
    """
    max_length = 0
    current_length = 0
    last_seen = {}

    for index, char in enumerate(origin):
        if char in last_seen and last_seen[char] >= current_length:
            current_length = last_seen[char] + 1
        else:
            current_length += 1

        last_seen[char] = index
        max_length = max(max_length, current_length)

    return max_length