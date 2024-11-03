import json
import pandas as pd
import utils
import ds_methods


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

# initialization
users, items = utils.generate_users_items_list(data)
matrix, m, n = utils.generate_matrix(users, items, data)

# splitting matrix into training/testing
matrix, testing_data = utils.training_split_matrix(matrix)

# descriptive measures
mean_rating_by_user, mean_rating_by_item = ds_methods.find_user_item_mean_ratings(users, items, matrix)
matrix_mean = ds_methods.find_matrix_mean(matrix)


# this part isn't finished yet, but I got tired. Probably I will finish it later, but you can still use it as is

for i in range(m):
  for j in range(n):
    if matrix[i][j] == 0:
      matrix_mean_method_prediction = ds_methods.matrix_mean_method(matrix_mean)
      baseline_estimate_method_prediction = ds_methods.baseline_estimate_method(users, items, matrix_mean, mean_rating_by_user, mean_rating_by_item, i, j)
      # to create a new way of predicting a rating, create variable your_method_prediction = ... here
      
      matrix[i][j] = {
        'overall_predictions': [
          {'matrix_mean_method': matrix_mean_method_prediction},
          {'baseline_estimate_method': baseline_estimate_method_prediction}
          # and then add it to the overall predictions list in this format
          ]}



evaluation_results =  ds_methods.evaluate_recommendation(matrix, testing_data)

for key, value in evaluation_results.items():
  for entry in evaluation_results[key]:
    print(key, entry)


# uncomment this if you want to see the matrix
# utils.displayMatrix(m, n, matrix)



