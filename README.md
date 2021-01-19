![Python application test with Github Actions](https://github.com/postBG/FlaskML.udacity/workflows/Python%20application%20test%20with%20Github%20Actions/badge.svg)

# FlaskML.udacity

## Overview

The goal of this project is to learn how to build a continuous delivery pipeline using Azure. When you push a new commit to the project, the built pipeline will build, test, and deploy the change to your azure service. You can refer to the below image. 

![Overall Architecture](resources/architecture.png)

### Project Plan

We adopt spreadsheet and Trello as a weekly planner and a ticket system, respectively.
We share our plan using the links to the spreadsheet and Trello board:

* [The link to the spreadsheet](https://docs.google.com/spreadsheets/d/13OMxyuo_yzPh713XNW5niLp2SbMff53pCP-qgk3LD7A/edit?usp=sharing)
* [The link to the Trello board](https://trello.com/b/ruJQ2aIj/flaskml)


### Prerequisites

You need to create the following accounts:

* [A github account](https://github.com/)
* [An Azure account and an activated Azure cloud shell](https://azure.microsoft.com/en-us/free/)


## Instructions

### 1. Set Up the Project and Run Local Test

First, you need to clone this project on your Azure Cloud Shell.
The result will be similar to the following image:
![screen_clone](resources/clone_repo.png)

Run the below commands and check whether the code passes the local tests.

```bash
~$> cd FlaskML.udacity
~/FlaskML.udacity$> make all
```

If successful, you will get results similar to the following image:
![](resources/make_all_first.png)

### 2. Configure Github Action as a Continuous Integration Pipeline

First, go to your GitHub repository and enable Github Action.
Checkout the provided [yml file](https://github.com/postBG/FlaskML.udacity/blob/main/.github/workflows/main.yml) configuring the automated build, lint, and test.
If you enabled Github Action correctly, Github Action would build the code automatically, and you will get the following results:
![](resources/github_action_pass.png)

### 3. Implement a Continuous Delivery Pipeline with Azure Pipeline

Before implementing a continuous delivery pipeline, you need to deploy the Flask Application with Azure Web App.










