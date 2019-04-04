import json

# while True:
	# name = input('What is your name?')
	# surname = input('What is your surname')
	# age = input('How old are you?')

#     # with open("info_.json", "w") as data:
#     #     information = {name: {'surname': surname, 'age': age}}
#     #     data.write(json.dumps(information))
#     #     data.close()

	# with open("info_.json", "a") as data:
	# 	information = {name: [{'surname': surname, 'age': age}]}
	# 	data.write(json.dumps(information))
	# 	data.close()
# 	with open("info_.json", "r") as info_read:
# 		dict_info = json.loads(info_read.read())
# 		name_d = dict_info.get(name)
# 		print(name_d)


with open('info_.json') as json_file:  
	data = json.load(json_file)
	for p in data['papa']:
		print('surname: ' + p['surname'])
		print('age: ' + p['age'])
		print('')

# dict1 = {}
# dict2 = {}
# json.dumps([dict1, dict2])
# json.loads(json.dumps([dict1, dict2]))