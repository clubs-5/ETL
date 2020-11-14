import json
import io

file = input('Give me a json file name without extension: ')
g = open('{}.json'.format(file), 'r', encoding= 'utf8')
data = json.load(g.read())
uni = []

for i in data:
    if i not in uni:
        uni.append(i)

jstring = json.dumps(uni)

with open("{}_fixed.json", 'a', encoding='utf8') as obj:
    obj.write(jstring)



