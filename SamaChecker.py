import sys

file1 = sys.argv[1]
file2 = sys.argv[2]
buka1 = open(file1,"r")
buka2 = open(file2,"r")
for i in range(200000):
    if(buka1.readline(i) != buka2.readline(i)):
        print ("OUTPUT NOT SAME FOUND!\n" + buka1.readline(i) + "!=\n" + buka2.readline(i))
        break;
print ("done")
