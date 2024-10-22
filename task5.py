students = [
    {"name": "Ally", "score" : [42, 48]},
    {"name": "Betty", "score" : [68, 45]},
    {"name": "Kirby", "score" : [90, 85]},
    {"name": "Samuel", "score" : [35, 55]}
]

scores = [i["score"] for i in students]


x, y = scores[0]

average_list = []
for x, y in scores:
    average_list.append((x+y)/2)

pass_or_fail = ["passed the lesson" if i >= 50 else "failed the lesson" for i in average_list]


# Creating a dictionary of names and pass/fail status
pass_or_fail_dict = {student["name"]: result for student, result in zip(students, pass_or_fail)}

pass_or_fail_dict
    
