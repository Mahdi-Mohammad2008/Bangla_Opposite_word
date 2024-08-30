import random as r

quostion=int(input("Enter how many quostion you want to ans: "))
with open('opposite_word.txt', 'r',encoding='utf-8')as f:
    lines = f.readlines()

oppsiteDict = {}
for line in lines:
    parsed = line.split("\t")
    oppsiteDict[parsed[0]] = parsed[1]

all_key=list(oppsiteDict.keys())
all_value=list(oppsiteDict.values())
i = 1
for ii in range(quostion):
    key=r.choice(all_key)
    print(f"Q{i}. What is the opposite of {key}?")

    value=oppsiteDict[key]
    options = all_value.copy()
    options.remove(value)
    random_options = r.sample(options, 3)
    random_options.append(value)
    r.shuffle(random_options)
    
    a=0
    for option in random_options:
        print(f"{chr(65+a)}. {option}")
        a += 1
    ans = input("Ans: ")
    if ans.upper() == chr(65 + random_options.index(value)):
        print("Correct")
    else:
        print("Incorrect")
        print(f"Correct ans is {value}")
    i+= 1

