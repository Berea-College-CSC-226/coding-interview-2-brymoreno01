def main():
    sentence = "This is the longest word"
    lastword = ""
    sentence.split()
    for word in sentence.split():
        if lastword > len(word):
            lastword += word
            print(lastword)
        elif lastword < len(word):
            return print(lastword)

main()