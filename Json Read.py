import json

File = open("C:\\Users\\Asif\\Desktop\\Practice\\Python\\Json Practice\\User.json", 'r')

# jsonRead = File.read()
readJson = json.loads(File.read())
# print(readJson)
# name =input()
for i in readJson:
    if i['id'] == 560:
        i['name'] = input("Enter name: ")
    print(i)
# print(readJson)
out_file = open("C:\\Users\\Asif\\Desktop\\Practice\\Python\\Json Practice\\User.json", 'w')

json.dump(readJson, out_file, indent=3)

# out_file.close()
# json.dump()
# print(readJson[0]['name'])
# print(readJson[0]['id'])
