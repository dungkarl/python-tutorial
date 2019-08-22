"""
    List, Tuples, Sets
"""

# list
langues = ['Python', 'Java', 'C#', 'Kotlin']
nums = [2, 3 ,4, 1, 6, 7, 8]
print(langues)
print(len(langues))
print(langues[0])

#print("Min:", min(langues))

for lang in langues:
    print(lang)

print(langues[0:3])
print(langues[-1])
langues.append('C++')
print(langues)

sorted(langues)
new_nums = sorted(nums)
print(new_nums)
print(nums)
print(min(new_nums))
print("Index of Python: ", langues.index('Python'))

langues_str = '-'.join(langues)
print(langues_str)


# tuple

tuple_1 = ('Python', 'Java', 'C#', 'Kotlin')
tuple_2 = tuple_1
#tuple_1[0] = 'New'
print(tuple_1)
print(tuple_2)


# sets

set_langues = {'Python', 'Java', 'C#', 'Kotlin'}
new_set_langues = {'Python', 'C++', 'Go', 'Kotlin'}

print('Python' in set_langues)

print(set_langues)
print(set_langues.intersection(new_set_langues))
print(set_langues.difference(new_set_langues))
print(set_langues.union(new_set_langues))
