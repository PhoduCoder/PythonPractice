#Author: Gaurav Parashar


student=[['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

student_dict=dict(student)

print(type(student_dict), student_dict)

print("============")

print(min(student_dict.values()))


print("============")


min_element=(min(student_dict.items()))

student_dict.popitem(min_element)

second_min_element=(min(student_dict.items()))

print(second_min_element)
