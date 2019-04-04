import json

with open('data3.json','w') as out:
	json.dump('data3.json',out)

jstr =json.dumps(data,indent =4)
print(jstr)