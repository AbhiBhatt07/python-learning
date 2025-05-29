# funtion of count the words


def count_word(filename):
    with open(filename, "r") as file:
        text = file.read()

    words = text.lower().split()

    word_freq = {}

    # loop through each word in list

    for word in words:
        word = word.strip('.,/!"()[]{}?')

        word_freq[word] = word_freq.get(word, 0) + 1

    sorted_word = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

    # Print a header for the top results
    print("Top 10 most frequent words:\n")


    for word, frequncy in sorted_word:
        print(f"{word}: {frequncy}")


count_word("sample.txt")