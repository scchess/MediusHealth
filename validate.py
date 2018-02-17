
lines = []
with open('data.tsv', 'r') as r:
    for line in r:
        lines.append(line.split('\t')[1])

with open('A.txt', 'r') as r:
    for line in r:
        key = line.split('\t')[0]
        n = 0
        for line in lines:
            for word in line.strip().split(' '):
                if word == key:
                    n += 1
        print(str(key) + '\t' + str(n))        