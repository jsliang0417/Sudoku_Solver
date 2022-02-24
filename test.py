line = open("test.txt", 'r')

for i in range(3):
    lines = line.readline().rstrip('\n')
    print(lines)