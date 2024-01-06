def decode(file_path):
    with open(file_path, 'r') as file:
        content = file.read().split()

    number_word_pairs = [(int(content[i]), content[i+1]) for i in range(0, len(content), 2)]
    number_word_pairs.sort(key=lambda x: x[0])

    message_words = []
    total_numbers_in_line = 1
    current_line_end = 0

    for number, word in number_word_pairs:
        current_line_end += 1
        if current_line_end == total_numbers_in_line:
            message_words.append(word)
            total_numbers_in_line += 1
            current_line_end = 0

    return ' '.join(message_words)

print(decode('message_file.txt'))
