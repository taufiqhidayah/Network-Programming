import json

# data = {}  
# data['people'] = []  
# data['people'].append({  
#     'name': 'Scott',
#     'website': 'stackabuse.com',
#     'from': 'Nebraska'
# })
# data['people'].append({  
#     'name': 'Larry',
#     'website': 'google.com',
#     'from': 'Michigan'
# })
# data['people'].append({  
#     'name': 'Tim',
#     'website': 'apple.com',
#     'from': 'Alabama'
# })

# name = input('What is your name?')
# website = input('What is your surname')
# from1 = input('How old are you?')
# # {"people": [{"name": "Scott", "website": "stackabuse.com", "from": "Nebraska"}

# with open("data2.txt", "a") as data:
#   information = {'people': [{'name': name, 'website':website ,'from':from1 }]}
#   data.write(json.dumps(information))
#   data.close()

# with open('data2.txt', 'w') as outfile:  
#     json.dump(data, outfile)

with open('data2.txt') as json_file:  
    data = json.load(json_file)
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')