import random
import pandas
numbers=[3,4,6,8,9,10]

new_list=[]
for i in numbers:
    new_list.append(i+1)
name="rohini"    
# print(new_list)    
n_list=[i*2 for i in numbers]
# print(n_list)

rho=[n*2 for n in range(len(name)) if n%2==0]
# # print(rho)
names=["rohini","ram","ayansh","ravi","sunny"]
new_names=[i.upper() for i in names if len(i)>4]
# print(new_names)

student_marks={n:random.randint(0,100) for n in names}

# print(student_marks)

passed_students={student:score for student,score in student_marks.items() if score>50}
# print(passed_students)



data_student={"naame":["rohini","ram","ayansh","ravi","sunny"],
              'marks':[95,84,50,35,43],
              'id':[489,488,560,390,256]
              }
pand_students=pandas.DataFrame(data_student)
# # print(pand_students)

# for (index,row) in pand_students.iterrows():
#     # if row.naame=="ram":
#       print(row.naame)

# nato alphabet program

natodata=pandas.read_csv("nato_alphabets.csv")
# print(natodata)
# dicnato=natodata.to_dict() # this will give different output i.e with index and values
# print(dicnato)
nato={row.letter:row.code for (index,row) in natodata.iterrows()}
# print(nato)
user_name=input("yoour word: ").upper()
natolst1=[i for i in user_name]
# print(natolst1)
   

nato_output=[nato[letter] for letter in natolst1]
print(nato_output)