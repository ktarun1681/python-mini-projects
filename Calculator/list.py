import sys
my_file = open(sys.argv[1])
for line in my_file:
     line = line.strip()
     currentline = line.split(" ")
     leng = len(currentline)
     num = int(str(currentline[leng-1]))
     currentline.pop(leng-1)
     if num <= leng - 1:
          print str(currentline[-1*num])
my_file.close()