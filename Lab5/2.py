sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}
for key, value in sample_dict.items():
    print(f'{key:<10}key:{value:>10}')

for key in sample_dict.key():
    print(key, sample_dict[key])

newdict={}
l1=["age","salary","name","aboo"]
for key in l1:
    if key in sample_dict:
        newdict[key]=sample_dict[key]
print(newdict)

for i in l1:
    print(sample_dict.pop(1,"Bland"))
print(sample_dict)

if 'Jones' in sample_dict.values():
    print("yes")
else:
    print("No")

sample_dict["location"] = sample_dict.pop("city")
print(sample_dict)