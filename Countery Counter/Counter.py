def main():
    file = open('text.txt', 'r')
    str =file.read()#read until white space
    uppercount = 0
    lowercount = 0
    digitcount = 0
    whitespace = 0

    for word in str:
        if(word.isupper()):
            uppercount += 1
        elif(word.islower()):
            lowercount += 1
        elif(word.isdigit()):
            digitcount += 1
        elif(word.isspace()):
            whitespace += 1

    print("Uppercase letters:", uppercount)
    print("Lowercase letters:", lowercount)
    print("Digits:", digitcount)
    print("Spaces:", whitespace)
main()