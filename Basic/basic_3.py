"""
	Dictionaries
"""

profile = {
	'name':'DungKarl',
	'age':30,
	'langues':['Python', 'Java', 'React']
}

profile['phone'] = 123456789

print(type(profile['langues']))

print(profile['name'])

print(profile.get('phone', 'Not Found'))

for k, v in profile.items():
	print("Key:{} - Value:{}".format(k,v))