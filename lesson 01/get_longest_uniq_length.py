def get_longest_uniq_length(origin: str, /) -> int:
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

def main():
    user_input = input("Введите строку: ")
    result = get_longest_uniq_length(user_input)
    print(result)

if __name__ == "__main__":
    main()