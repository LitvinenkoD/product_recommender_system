
### General purpose functions related to coding routines go here


import pandas as pd
import tkinter as tk
from tkinter import ttk
import random as rd


def generate_users_items_list(data):
  users = set()
  items = set()
  for entry in data:
    users.add(entry['reviewerID'])
    items.add(entry['asin'])

  users = sorted(list(users))
  items = sorted(list(items))
  return (users, items)


def generate_matrix(users, items, data):
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
  
  return (matrix, m, n)



# Testing / Training split
# testing data is a list of all entries we popped, as well as their indeces in the original matrix
def training_split_matrix(matrix):
  m, n = (len(matrix), len(matrix[0]))

  testing_ratio = .2
  testing_data = []
  for i in range(m):
    user_ratings_indeces = []
    for j in range(n):
      if matrix[i][j] != 0:
        user_ratings_indeces.append((i, j))

    ratings_count = len(user_ratings_indeces)
    number_of_reviews_to_remove = round(ratings_count * testing_ratio)

    random_indeces = rd.sample(range(len(user_ratings_indeces)), number_of_reviews_to_remove)

    for random_index in random_indeces:
      i, j = user_ratings_indeces[random_index]

      # copy the real data to a testing data list, set matrix value to 0
      test_index_real_data = matrix[i][j]['overall']
      matrix[i][j] = 0

      testing_data.append(((i, j), test_index_real_data))
  
  return (matrix, testing_data)




# Matrix visualizer
def displayMatrix(m, n, matrix):
  
  df = pd.DataFrame(matrix)

  # Initialize Tkinter
  root = tk.Tk()
  root.title(f"{m}x{n} Matrix")

  # Create a Treeview widget for displaying the DataFrame
  tree = ttk.Treeview(root)

  # Define columns based on DataFrame
  tree["columns"] = list(df.columns)
  tree["show"] = "headings"  # Hide first empty column

  # Add column headers
  for col in df.columns:
    tree.heading(col, text=str(col))

  # Insert DataFrame rows into Treeview
  for index, row in df.iterrows():
    tree.insert("", "end", values=list(row))

  # Add horizontal and vertical scrollbars
  h_scroll = ttk.Scrollbar(root, orient="horizontal", command=tree.xview)
  v_scroll = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
  tree.configure(xscrollcommand=h_scroll.set, yscrollcommand=v_scroll.set)
  h_scroll.pack(side="bottom", fill="x")
  v_scroll.pack(side="right", fill="y")

  # Pack the Treeview widget
  tree.pack(expand=True, fill="both")

  # Run the Tkinter main loop
  root.mainloop()