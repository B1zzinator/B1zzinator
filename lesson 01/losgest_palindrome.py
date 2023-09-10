def get_longest_palindrome(origin: str) -> str:

    def is_palindrome(s):
        return s == s[::-1]

    longest_palindrome = ""
    for i in range(len(origin)):
        for j in range(i + 1, len(origin) + 1):
            substring = origin[i:j]
            if is_palindrome(substring) and len(substring) > len(longest_palindrome):
                longest_palindrome = substring

    return longest_palindrome
print(get_longest_palindrome("sgaffs"))
print(get_longest_palindrome("1012210"))