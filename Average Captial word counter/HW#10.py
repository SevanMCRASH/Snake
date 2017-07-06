def main():
    sum = 0
    file = open('text.txt', 'r')
    filename = file.read()
    lists = filename.split()

    for word in lists:
        if('.' in word) or ('?'in word):
            sum += 1

    average = len(lists)/ sum
    print("Average number of words per sentence:"," %.2f"%average)

    file.close()
main()