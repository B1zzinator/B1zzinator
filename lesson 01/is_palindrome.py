from typing import Union
def is_palindrome(origin: Union[str, int], /) -> bool:
    origin_str = str(origin).lower()
    origin_str = ''.join(e for e in origin_str if e.isalnum())

    left, right = 0, len(origin_str) - 1

    while left < right:
        if origin_str[left] != origin_str[right]:
            return False
        left += 1
        right -= 1

    return True

# Примеры использования
print(is_palindrome("aba"))
print(is_palindrome("abc"))
print(is_palindrome(12345))
print(is_palindrome(12321))