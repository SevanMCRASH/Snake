def main():
    name = input("Enter a name to search or type QUIT to exit:\n")
    while(name.lower() != "quit"):
        position, flag = positionfinder(name,'BoyNames.txt')
        position2, flag2 = positionfinder(name,'GirlNames.txt')
        if(flag == True and flag2 == True):
            print("The name '",name.capitalize(), "' was found in both lists: boy names (line ", position + 1, ") and girl names (line ", position2 +1, ").",sep= '')
        elif(flag == True):
            print("The name '", name.capitalize(), "' was found in popular boy names list (line ",position+1, ").",sep= '')
        elif(flag2 == True):
            print("The name '",name.capitalize(),"' was found in popular girl names list (line ", position2+1,").",sep= '')
        else:
            print("The name '", name.capitalize(), "' was not found in either list.",sep= '')

        name = input("Enter a name to search or type QUIT to exit:\n")

def positionfinder(name,filename):
    position = 0
    flag = False
    arrName = []
    with open(filename) as file:
        for line in file:
            line = line.strip()  # or someother preprocessing
            arrName.append(line)

    for i in range(200):
        if(name.lower() == arrName[i].lower()):
            flag = True
            position = i
    return position, flag;
main()