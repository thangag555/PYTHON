import json
emp={
  "principal": ["raj kumar"],
  "teachers": ["vimal","arun"],
  "students": ["bala","sathish","ganesh"],
  "address": "madurai",
  "married": False,
  "single": None
}


'''file=open("data2.json","w")
json.dump(emp,file)
file.close()'''

file=json.dumps(emp)
print(file)


'''file=open("data2.json","r")
a=json.load(file)
file.close()
print(a)'''

#file=open("data2.json","r")
a=json.loads(file)
print(a)
