# Deployment of Machine Learning Models

Accompanying repo for the online course Deployment of Machine Learning Models.

For the documentation, visit the [course on Udemy](https://www.udemy.com/deployment-of-machine-learning-models/?couponCode=TIDREPO).


# Section 4:

It puts together a pipeline in a research environemnt - i.e., jupyter notebooks

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

It puts everything into production - i.e., creates a package.

section-05-production-model-package/
If we run in that directory: tox -e train
It runs regression_model/train_pipeline.py to train the model.
And it creates a .pkl file in regression_model/trained_models/

tox: is a virtual environment management tool

To specify an environemnt defined in the tox.ini between [environemnt]:
run: tox -e <environment>

To train model and run tests, run: tox -e test_package

To build the package: python3 -m build
It will create: dist/, build/, ...egg-info/


Assignment in my-assignment-section-05/.
It puts into production what we did earlier for titanic.


# Section 6:

Build an API to serve our model predictions.

section-06-model-serving-api/
run: tox -e run

It runs a server locally.
If we go to http://localhost:8001/, we go to the API.
If we go to POST we can run predictions.

Here we are using FastAPI (other examples are Flask and Django).
Create example of FastAPI in section-06-model-serving-api/fastapi-quick-demo/
Run by doing: python -m uvicorn main:app --reload

http://127.0.0.1:8000/ --> returns Hello World
http://127.0.0.1:8000/square?num=2 --> returns 4


Now we are going to use Railway App and PaaS.
https://railway.app/dashboard

* Install railway CLI.
* Log in: railway login --browserless
* It will show a link, and there I have to verify it's me
* In the web:
* create new project: empty project
* in the project, create new empty service
* in terminal, run: railway link
* and select project, environment, and service
* then, run: railway up --detach
* I think the alternative would be to just run: railway up --detach --service <service_id>, but right now, I can't find the service_id.
* In service, go to settings, under networking generate domain
* this will produce a link in which we can access our API


# Section 7:

In this section we will use CicleCI to automate the deployment.
Other options are: Jenkins, Travis CI, Bamboo, GitlabCI

Log in to https://app.circleci.com/
And log in with github account.
Go to Projects and press 'Set Up Project'.
This will connect our repo to circleCI.
The repo needs to have a repo/.circleci/config.yml file to define the configuration

We need to add environment variables:
Go to project, go to project settings.
Then, environment variables:
RAILWAY_TOKEN:
  - asd
GEMFURY_PUSH_URL:
  - asd

There are 3 steps in this section:
- section_07_test_app: runs tests
- section_07_deploy_app_to_railway: deploys api in railway
- section_07_test_and_upload_regression_model: builds the package and publishes to GEMFURY

GEMFURY



# Section 8:

# Section 9:

# Section 10:

# Section 11:

# Section 12:

# Section 13: