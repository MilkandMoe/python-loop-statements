genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

list = genres[0:4:1]
print(list)
list2 = genres[1:4:1]
print(list2)


import random
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
for x in range(len(genres)):
    genres.append("Music")
    print(f'x, {genres}')
    
    


for i in range(10,0,1):
    print(f"{i}, The beat drops now!")