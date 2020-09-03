scores = []

result_f = open("results.txt")

for line in result_f:
    (name, score) = line.split()
    scores.append(float(score))
result_f.close()

i = 0

while i < 3:
    print(scores[i])
    i += 1
