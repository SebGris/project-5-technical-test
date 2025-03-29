words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]


def count_vowels(word):
    """Count the number of vowels in a word."""
    vowels = "aeiouy"
    count = 0
    for char in word:
        if char.lower() in vowels:
            count += 1
    return count


def main():
    """Main function to count vowels in a list of words."""
    list = [(word, count_vowels(word)) for word in words]
    print(list)


if __name__ == "__main__":
    main()
