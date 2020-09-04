scores = []
names = []

result_f = open("results.txt")

for line in result_f:
    (name, score) = line.split()
    names.append(name)
    scores.append(score)

names.sort(reverse = True)
scores.sort(reverse = True)

i = 0

while i < 3:
    print(names[i] +"\t" +scores[i])
    i = i + 1

