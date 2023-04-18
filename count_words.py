import os

def count_words_in_file(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
        words = text.split()
        word_count = len(words)
    return word_count

def find_transcripts_and_count_words(start_directory):
    word_counts = {}
    total_word_count = 0
    
    for root, _, files in os.walk(start_directory):
        for file in files:
            if file == "000-full_transcript.md":
                file_path = os.path.join(root, file)
                word_count = count_words_in_file(file_path)
                word_counts[file_path] = word_count
                total_word_count += word_count
    
    return word_counts, total_word_count

if __name__ == '__main__':
    start_directory = input("Enter the path to the directory containing the conversations: ")
    word_counts, total_word_count = find_transcripts_and_count_words(start_directory)

    print("\nWord Counts for '000-full_transcript.md' Files:")
    for file_path, word_count in word_counts.items():
        print(f"{file_path}: {word_count} words")
    
    print(f"\nTotal word count across all '000-full_transcript.md' files: {total_word_count} words")

