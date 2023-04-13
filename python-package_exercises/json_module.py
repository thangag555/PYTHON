import json
from difflib import get_close_matches
jsonfile=json.load(open("data1.json"))
word=input("enter the word:")
def check(d):
    d=d.lower()
    if d in jsonfile:
        return jsonfile[d]
    elif len(get_close_matches(d,jsonfile.keys()))>0:
        choice=input("did you mean %s , enter Y for yes, N for no " %get_close_matches(d,jsonfile.keys())[0])
        if choice=="Y" or "y":
            return jsonfile[get_close_matches(d,jsonfile.keys())[0]]
        elif choice=="N" or "n":
            return "the word does not exists,please enter the correct word"
        else:
            return "you entered the wrong choice"
    else:
        return "the word doesn't exists,please enter the correct word"

result=(check(word))
print(result)
"""if type(result)==list:
    for i in result:
        print(i)
else:
    print(result)"""

