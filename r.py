fname = input("Enter the file name : ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened :", fname)
else:
    count = 0 
    for line in fhand:
        if line.startswith("From:"):
            line = line.rstrip()        
            print(line)
            count = count + 1
    print('Total %d lines starts with "From:" ' % count)
    fhand.close()
