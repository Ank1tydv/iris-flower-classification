# Iris Flower Classification

This project implements an **Iris Flower Classification** machine learning model using the famous Iris dataset. The goal of this project is to predict the species of the iris flower based on its features such as sepal length, sepal width, petal length, and petal width.

## Table of Contents
- [About the Project](#about-the-project)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Model Evaluation](#model-evaluation)
- [Contributors](#contributors)

## About the Project

This project uses the Iris dataset to train a Random Forest Classifier and classify iris flowers into 3 species:
- Setosa
- Versicolor
- Virginica

The project covers data preprocessing, model training, evaluation, and deployment using Flask and Docker.

## Installation

To get started with this project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Ank1tydv/iris-flower-classification.git
   cd iris-flower-classification

2. Install required dependencies:
	pip install -r requirements.txt
3. Make sure you have Docker and Flask set up if you're running the model in a containerized environment.

## Usage

1. To train the model:
	python src/train.py

2. To run the model locally using Flask:
	python src/app.py
3. To use the API for predictions, you can make a POST request to
	 http://127.0.0.1:5000/predict.

## Technologies Used
Python
Pandas (for data processing)
scikit-learn (for machine learning model)
Flask (for creating the API)
Docker (for containerization)
AWS ECR (for model deployment)


## Model Evaluation
The model's performance was evaluated using the accuracy score on the test dataset. The Random Forest Classifier achieved an accuracy of approximately XX%.

Contributors
Ankit Yadav - GitHub Profile :https://github.com/Ank1tydv
Feel free to contribute to this project by submitting issues or pull requests.

