from pymongo import MongoClient


# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb://192.168.33.101:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')
result = client['TVShows']['ff'].aggregate([
    {
        '$project': {
            '_id': 0, 
            'Show': 1, 
            'tomato': {
                '$objectToArray': '$tomato'
            }
        }
    }, {
        '$project': {
            'tomato.v.Year': 0, 
            'tomato.v.consensus': 0, 
            'tomato.v.Reviews': 0
        }
    }, {
        '$project': {
            'Show': 1, 
            'tomato': {
                '$arrayToObject': '$tomato'
            }
        }
    }
])

#print(type(result))

for i in result:
    x = 1
    show_tomato = []
    name = i['Show']
    while i['tomato']:

        if x < 21:

            try: 
                if i['tomato']['Season {}'.format(x)]:
                    print('Season {} exists'.format(x))
                    print
        
            except:
                print('Season {} DNE'.format(x))

        else:
            break
        #x += 1
        break
# with open('out.csv', 'a', encoding='utf8') as obj:
#     for i in result:

    