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
            'tomato.v.User_ratings': 0, 
            'tomato.v.Year': 0, 
            'tomato.v.audience_score': 0, 
            'tomato.v.Critic_Ratings': 0, 
            'tomato.v.tomatometer': 0, 
            'tomato.v.consensus': 0
        }
    }, {
        '$project': {
            'tomato.v.Reviews.name': 0, 
            'tomato.v.Reviews.org': 0
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

for i in result:
    x = 1
    show=i['Show']
    
    while i['Show']: 
        if x < 21: #iterate through each available season, assuming no more than 20 seasons
            try:
                season = i['tomato']['Season {}'.format(x)]
                if season:
                    print('Season {}'.format(x))
                    for review in season['Reviews']:
                        with open('{name}_s{num}.txt'.format(name=show,num=x),'a', encoding='utf8') as txt:
                            txt.write(review['content'] + '\n')
                        print(review['content'])
                print("================")

            except:
                pass

        else:
            break
        x += 1
    
    #print(i['tomato']['Season 1']['Reviews'][0]['content'])
    break