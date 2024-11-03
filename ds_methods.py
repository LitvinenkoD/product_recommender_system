
### Functions that are related to the Data Science aspect of the project go here

def find_matrix_mean(matrix):
  sum = 0
  count = 0
  for row in matrix:
    for elem in row:
      if elem != 0:
        sum += elem["overall"]
        count += 1
  
  if count == 0:
    return None
  
  mean = sum / count
  return float(f"{mean:.2f}")



## Finding mean rating by user and by item
def find_user_item_mean_ratings(users, items, matrix):

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
  
  return (mean_rating_by_user, mean_rating_by_item)



def evaluate_recommendation(matrix, testing_data):
  (i, j) = testing_data[0][0]
  number_of_methods_used = len(matrix[i][j]['overall_predictions'])
  method_names = [list(prediction.keys())[0] for prediction in matrix[i][j]['overall_predictions']]

  total_abs_error = [0 for _ in range(number_of_methods_used)]
  total_square_error = [0 for _ in range(number_of_methods_used)]

  for entry in testing_data:
    (i, j) = entry[0]
    actual_value = entry[1]

    for index, prediction in enumerate(matrix[i][j]['overall_predictions']):
      predicted_value = list(prediction.values())[0]

      total_abs_error[index] += abs(actual_value - predicted_value)
      total_square_error[index] += ((actual_value - predicted_value) ** 2)


  mean_absolute_error = [total_abs_error[i] / len(testing_data) for i in range(number_of_methods_used)]
  root_mean_square_deviation = [(total_square_error[i] / len(testing_data)) ** (1/2) for i in range(number_of_methods_used)]


  return {
    "MAE": [{method_names[i]: mean_absolute_error[i]} for i in range(number_of_methods_used)],
    "RMSD": [{method_names[i]: root_mean_square_deviation[i]} for i in range(number_of_methods_used)]}


# baseline estimate
def user_item_baseline_estimate(users, items, matrix_mean, mean_rating_by_user, mean_rating_by_item, i, j):
  baseline_estimate = matrix_mean
  if mean_rating_by_user[users[i]]:
    user_bias = mean_rating_by_user[users[i]] - matrix_mean
    baseline_estimate += user_bias

  if mean_rating_by_item[items[j]]:
    item_bias = mean_rating_by_item[items[j]] - matrix_mean
    baseline_estimate += item_bias

  return baseline_estimate




# Rating prediction methods

# dummy example
def matrix_mean_method(matrix_mean):
  return matrix_mean

# a more sophisticated, but also code-primitive example
def baseline_estimate_method(users, items, matrix_mean, mean_rating_by_user, mean_rating_by_item, i, j):
  baseline_estimate = user_item_baseline_estimate(users, items, matrix_mean, mean_rating_by_user, mean_rating_by_item, i, j)
  return float(f"{baseline_estimate:.2f}")

