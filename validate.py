
lines = []
with open('data.tsv', 'r') as r:
    for line in r:
        lines.append(line.split('\t')[1])

with open('A.txt', 'r') as r:
    for line in r:
        toks = line.split('\t')[0]
        n = 0
        for line in lines:
            n += line.count(toks)
        print(str(toks) + '\t' + str(n))        