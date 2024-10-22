students = [
    {"name": "Ally", "score" : [42, 48]},
    {"name": "Betty", "score" : [68, 45]},
    {"name": "Kirby", "score" : [90, 85]},
    {"name": "Samuel", "score" : [35, 55]}
]

scores = [i["score"] for i in students]


x, y = scores[0]

total_list = []
for x, y in scores:
    total_list.append((x+y))

total_list

total_scores = [(150 - i) for i in total_list]
total_scores

total_scores = [i if i > 0 else 0 for i in total_scores ]
total_scores


final_scores_needed = {student["name"]: result for student, result in zip(students, total_scores)}

final_scores_needed
