import json
import pandas as pd
import utils


# B0006GVNOA


# all files
f1 = './Digital_Music_5.json' # mid
f2 = './Appliances_5.json'    # small
f3 = './Video_Games_5.json'   # large
f4 = './microdataset.json'    # extra small
f5 = './All_Beauty_5.json'    # mid small 5k <-- main dataset right now

data = []
with open(f5, 'r') as json_file:
  for line in json_file:
    data.append(json.loads(line.strip()))


data2 = pd.DataFrame(data)
# print(len(pd.unique(data2["reviewerID"])))
# print(len(pd.unique(data2["asin"])))



users = set()
items = set()
for entry in data:
  users.add(entry['reviewerID'])
  items.add(entry['asin'])

users = sorted(list(users))
items = sorted(list(items))


## Matrix initialization
m = len(users)
n = len(items)
matrix = [[0 for _ in range(n)] for _ in  range(m)]


## Matrix population
for entry in data:
  user = entry['reviewerID']
  item = entry['asin']

  user_index = users.index(user)
  item_index = items.index(item)

  data_of_interest = {'overall': entry['overall']}
  matrix[user_index][item_index] = data_of_interest


# utils.displayMatrix(m, n, matrix)

## Finding mean rating by user and by item

# User
mean_rating_by_user = {}
for i in range(len(users)):   # Fix i, iterate j
  user_ratings_sum = 0
  ratings_count = 0
  for j in range(len(items)):
    if matrix[i][j] != 0:
      user_ratings_sum += matrix[i][j]['overall']
      ratings_count += 1

  if ratings_count != 0:
    user_mean = user_ratings_sum / ratings_count
    mean_rating_by_user[users[i]] = user_mean
  else:
    mean_rating_by_user[users[i]] = None


# Item
mean_rating_by_item = {}
for j in range(len(items)):   # Fix j, iterate i
  item_ratings_sum = 0
  ratings_count = 0
  for i in range(len(users)):
    if matrix[i][j] != 0:
      item_ratings_sum += matrix[i][j]['overall']
      ratings_count += 1

  if ratings_count != 0:
    item_mean = item_ratings_sum / ratings_count
    mean_rating_by_item[items[j]] = item_mean
  else:
    mean_rating_by_item[items[j]] = None


print(len(mean_rating_by_user))
print(len(mean_rating_by_item))
      

