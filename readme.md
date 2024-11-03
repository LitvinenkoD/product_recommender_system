

current state:
takes in a dataset
creates a user-item matrix
splits the matrix into training/testing parts
performs rating prediction in 2 simple ways
evaluates MAE and RMSD errors and prints them on the screen



project files:
project.py - main file (intentionally made small)
utils.py - helper file with some helper functions that support the structure of the program
  * create matrix
  * split matrix
  * display matrix
  * etc

ds_methods.py a helper file with functions that somehow operate on data
  * find matrix mean
  * find mean per user / item
  * find user / item baseline estimate
  * evaluate the recommendations using MAE and RMSD



how to work with this program?
the key elements of the program are done, and except for minor changes, we only need to create new methods of recommendation



how to create a recommendation method?
if you look at the 2 methods that already exist, both are some sort of a function that returns the recommendation for the 
i, j element of the matrix. both rely on some known data.

matrix_mean_method is using matrix mean, which is computed in the main file and is available for use

baseline_estimate_method is using baseline estimate for each user-item pair, which in turn relies on the matrix mean, and the means of the
ith user and the jth item. 

both of these methods are just 1 line codes, but that is because they use fundamental descriptive measures that are computed beforehand.
the reason why I still created these 1 line functions for the mean and the base line estimate functions is to establish a format in which other
methods should be used, allowing for easy insertion of them into the existing file.

the only 1 rule all methods follow is that they take however many arguments you want, and output 1 number, which is the prediction for i,j

if you write your recommendation method in this format, you'll be able to simply insert it into the main file, in the same fashion
the other 2 methods are already used



note on the skeleton code
right now the matrix we're working with only contains the rating, that is we're not using anything from the review data except for the
user id, product id, and the rating value

this means that for now, there is no easy way to use natural language processing, or any other method that relies on more than just the
user-product rating. it should be easy to scale the program to allow that however, but I didn't do that yet.

right now, out of all the things we planned to implement, we can do SVD and various ML recommendations. If we'll want to also do NLP in future,
we can change the skeleton to allow that

As of now, ideally, there should be no need to change the program structure, and we can simply create and test new methods







potential improvements:

migrate to using only df instead of sets

duplicates - allBeauty dataset has duplicate entries, at least some of them have to do with different versions of the same product
this can be used in future (finding a mean is one of the options)