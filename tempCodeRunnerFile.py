def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            word_count = len(content.split())
            return word_count
    except FileNotFoundError:
        print("File not found.")
        return -1


def main():
    file_path = input("Enter the file path: ")
    word_count = count_words(file_path)
    if word_count != -1:
        print(f"Number of words in the file: {word_count}")


if __name__ == "__main__":
    main()
