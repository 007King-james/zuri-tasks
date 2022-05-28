# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename) as f:
        lines = f.readlines()
    
    return (lines)


def count_words(file):
    text = read_file_content("story.txt")
    # [assignment] Add your code here
    words = []
    text = read_file_content(file)

    for t in text:
        t = t.split()

        for i in t:
            words.append(i)
    print(words)
    final_dict = {}
    for word in words:
        final_dict[word] = words.count(word)

    print(final_dict)

count_words("story.txt")


