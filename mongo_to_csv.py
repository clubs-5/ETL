from pymongo import MongoClient
import pandas as pd


# Requires the PyMongo package.
# https://api.mongodb.com/python/current

#get desired json values
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

show_tomato = []
n =1
#iterate through each tv show (document is this case) to create a list of tuples
for i in result:
    x = 1
    
    name = i['Show']


    while i['Show']:

        if x < 21: #iterate through each available season, assuming no more than 20 seasons

            try: 
                season = i['tomato']['Season {}'.format(x)]
                if season:
                   s =  int(season['Critic_Ratings']) #Becasue I forgot to turn critic rating into integer while crawling
                   season_tuple = (name, x, season['User_ratings'], season['audience_score'], s, season['tomatometer'])
                   show_tomato.append(season_tuple) 
       
            except:
                pass

        else:
            break
        x += 1



#now we create a pandas dataframe 
df = pd.DataFrame(show_tomato, columns = ['Show', 'Season', 'User_Ratings', 'Audience_Score', 'Critic_Ratings', 'Tomatometer'])

#write to csv file

df.to_csv('./out_csv.csv', encoding='utf-8', index= False)
print(df)
# with open('out.csv', 'a', encoding='utf8') as obj:
#     for i in result:

    