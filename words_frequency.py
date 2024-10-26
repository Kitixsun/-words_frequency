import sys

def sorted_words_count(file_path, N):
    try:
        word_count = {}

        file_info = open(file_path, 'r')
        for line in file_info:
            words = line.split()
            for word in words:
                word = word.lower()
                if word not in word_count:
                    word_count[word] = 1
                else:
                    word_count[word] += 1

        sorted_words_count = sorted(word_count.items(), key=lambda x:x[1], reverse=True)

        for i in range(N):
            print(i+1, "- word:", sorted_words_count[i][0], "| times apperead:", sorted_words_count[i][1])
    except Exception as e:
        print("Error")


def main():

    if len(sys.argv) != 3:
        print("Usage: python script.py <file_path> <N>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    try:
        N = int(sys.argv[2])
    except ValueError:
        print("Error: 'N' should be an integer.")
        sys.exit(1)


    sorted_words_count(file_path, N)

if __name__ == '__main__':
    main()
