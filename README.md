# Deployment of Machine Learning Models

Accompanying repo for the online course Deployment of Machine Learning Models.

For the documentation, visit the [course on Udemy](https://www.udemy.com/deployment-of-machine-learning-models/?couponCode=TIDREPO).


# Section 4:

section-04-research-and-development/titanic-assignment/

* 01-predicting-survival-titanic-assignement.ipynb: (Assignment 1)
It does the data cleaning, some data exploratory analysis, and then trains/tests a LogisticRegression model.

* 03-titanic-survival-pipeline-assignment.ipynb: (Assignment 3)
It does the data cleaning, separates data into train/test, creates a class called: ExtractLetterTransformer which is a pre-processor to add in the pipeline, creates pipeline:
  * categorical imputation
  * adds missing indicator to numerical variables
  * imputes numerical variables
  * extracts first letter from cabin
  * places categories with low turn up into one category: 'Rare'
  * encodes categorical variables into k-1 variables
  * applies standardization
  * trains logistic regression model
Fits pipeline, outputs train and test performance metrics


# Section 5:

# Section 6:

# Section 7:

# Section 8:

# Section 9:

# Section 10:

# Section 11:

# Section 12:

# Section 13: