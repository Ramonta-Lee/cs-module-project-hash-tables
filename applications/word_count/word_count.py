counts = {}
def word_count(s):
    # Your code here
    
    ignore = ' : ; , . - + = / \ | [ ] { } ( ) * ^ & " '
    for x in s:
        if x in ignore:
            s = s.replace(x, " ")

    # joins the words together removes extra space then splits by a space
    s = " ".join(s.split())
    # print("s", s)

    # puts words in a list of strings separated by a comma
    new_s = s.split()
    # print("new", new_s)

    for c in new_s:
        c = c.lower()  # case insensitive
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1

    return counts
        



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))