'''f = open(r'myfile.txt')
#print(f.read())
print(f.readline())
print(f.readline())
print(f.readline())
f.close()'''


'''with open(r'myfile.txt') as f:
    for line in f:
        print(line)'''


f = open(r'myfile.txt')
try:
    for line in f:
        print(line)
finally:
    f.close()
