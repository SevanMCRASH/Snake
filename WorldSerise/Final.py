def main():
 num = WorldSeries('WorldSeriesWinners.txt')
 print("Total number of World Series games:",num)
 mydict = Save('WorldSeriesWinners.txt')
 WorldSerieschampions(mydict)
 str,count = MostTeam(mydict)
 print(str,"won", count, "times.")
def Save(filename):
 employee = dict()
 readfile = open(filename, 'r')
 for key in readfile.readlines():
   if key in employee:
    employee[key] += 1
   else:
    employee[key] = 1
 return employee

def WorldSeries(filename):
 count = 0
 readfile = open(filename, 'r')
 while readfile.readline():
   count += 1
 return count

def WorldSerieschampions(employee):
 count = 0
 for key in employee:
  if key in employee:
   count += 1
 print("Number of World Series champions:",count - 1)

def MostTeam(employee):
 count = 0
 tmpstr = ''
 for key in employee:
   if employee[key] > count:
    count = employee[key]
    tmpstr = key

 tmpstr = tmpstr.strip()
 print("The team that won most World Series games:", tmpstr)
 return tmpstr,count


main()