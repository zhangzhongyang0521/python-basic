# -*- coding:utf-8 -*-
'''
    @ description: according to height and weight to calc BMI
    @ author: tony.zhang
    @ date: 2020.06.20
'''
"""
    another format multiline comment
"""
print('''according to height and weight to calc BMI''')
# ================application begin================
# input your height and weight
height = float(input("your height:"))
weight = float(input("your weight:"))
bmi = weight / (height * height)

print("your bmi:" + str(bmi))
# judge your body shape
if bmi < 18.5:
    print("over light")
if 18.5 < bmi < 24.9:
    print("good fit")
if 24.9 < bmi < 29.9:
    print("over weight")
if bmi >= 29.9:
    print("to fat")

# over size content process,use () to link
content = ("Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments"
           "Some types, such as ints, are able to use a more efficient algorithm when")
print("content:" + content)
# !!!!!not recommend way to process over size content
value = "Return the canonical string representation of the object.\
For many object types, including most builtins, eval(repr(obj)) == obj."
print("value:" + value)
