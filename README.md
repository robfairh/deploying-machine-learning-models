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
* I think the alternative would be to just run: railway up --detach --service <service_name>
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

Link GEMFURY account to github: https://manage.fury.io/dashboard/robfairh
GEMFURY is a private python package index server.
Go to Tokens.
For learning purposes we used a full access token.
For deployment we would use both push tokens to upload things, and deploy tokens to read things.
The GEMFURY_PUSH_URL is https://<TOKEN>:@pypi.fury.io/USERNAME/

Another environment variable that we need to add to CircleCI:
KAGGLE_USERNAME
KAGGLE_KEY

This are needed for the model to automatically dowload the data:
Go to kaggle, to settings, create new API token.

To get the RAILWAY_TOKEN:
got to railway, select project, go to project settings, tokens: create token

There are 3 steps in this section:
- section_07_test_app: runs tests
- section_07_deploy_app_to_railway: deploys api in railway
- section_07_test_and_upload_regression_model: builds the package and publishes to GEMFURY

All of these run.


# Section 8:

In this one, it seems like we are doing the same thing we did before, but in an instance of docker.

The build process happens inside the docker container.
The file responsible for building the docker container is: section-08-deploying-with-containers/Dockerfile

*
The following is not necessary, but helps to visualize the process:
First we build the docker locally.
For that we run:
docker build --build-arg PIP_EXTRA_INDEX_URL=https://<TOKEN>:@pypi.fury.io/USERNAME/ -t house-prices-api:latest .
then run: 'docker images' to see the built images
To run locally: run -p 8001:8001 -e PORT=8001 house-prices-api
If we go to http://localhost:8001/, we go to the API.
If we go to POST we can run predictions.
*

There is only one job in the CircleCI workflow: section_08_deploy_app_container_via_railway

For this it requires to set the environment variables in CircleCI:
PIP_EXTRA_INDEX_URL which is the same url as GEMFURY_PUSH_URL

In this one, it deploys a docker container to railway.

The test passes in CI.
It gets there up to the point of building the docker container.
Now we need to see in railway, if it actually succeeded.



# Section 9:

# Section 10:

This one I couldn't do it.
Because AWS has changed considerably and I couldn't follow the videos.


# Section 11:

# Section 12:

# Section 13: