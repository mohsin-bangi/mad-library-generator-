import random
rname = input("Enter random name:-")
urname = input("Enter your name:-")
place = input("Enter place:-")

adjv = ["NICE","LOVELY","HANDSOME","CUTE","GREAT","HUMBLE"]
verbs = ["proposed to","talked to","laughed at","taught to"]
preposition = ["above","in","near the","around the","behind"]

print(random.choice(adjv)+" "+rname+" "+random.choice(verbs)+" "+urname+" "+random.choice(preposition)+" "+ place)
