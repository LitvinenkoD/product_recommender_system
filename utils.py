import pandas as pd
import tkinter as tk
from tkinter import ttk


def generate_matrix(users, items, data):
    pass



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