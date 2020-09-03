highest_score = 0
second_score = 0
third_score = 0

result_f = open("results.txt")

for line in result_f:
    (name, score) = line.split()
    if float(score) > highest_score:
        third_score = second_score
        second_score = highest_score
        highest_score = float(score)
    elif float(score) > second_score:
        third_score = second_score
        second_Score = float(score)
    else:
        third_score = float(score)
    
result_f.close()

print("The highest score was: " + str(highest_score))
print("The second score was: " + str(second_score))
print("The third score was: " + str(third_score))

