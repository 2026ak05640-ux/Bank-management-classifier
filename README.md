# Bank-management-classifier
Machine Learning Classification Project

A. Problem Statement
The objective of this project is to implement and compare five machine learning classification algorithms using the Bank Marketing Dataset.
The project aims to predict whether a customer will subscribe to a term deposit based on customer information and previous marketing campaign details.

The five classification algorithms implemented are:

Logistic Regression
Decision Tree Classifier
K-Nearest Neighbors (KNN)
Gaussian Naive Bayes
Support Vector Machine (SVM)
The models are evaluated using six performance metrics: Accuracy, AUC Score, Precision, Recall, F1 Score, and Matthews Correlation Coefficient (MCC).


B. Dataset Description

Dataset Name: Bank Marketing Dataset

Source: UCI Machine Learning Repository

Dataset Link: https://archive.ics.uci.edu/dataset/222/bank+marketing

Problem Type: Binary Classification

Number of Instances: 45,211 (Bank Marketing bank-full version)

Number of Input Features: 16

Target Variable: y

Target Classes:
Yes (1): Customer subscribed to a term deposit.
No (0): Customer did not subscribe to a term deposit.
The dataset contains numerical and categorical attributes related to customers and marketing campaigns.


Data preprocessing includes:

Encoding categorical variables using OneHotEncoder.
Standardizing numerical features using StandardScaler.
Splitting the dataset into 80% training and 20% testing data.
Using stratified sampling to maintain the target class distribution.

C. GitHub Repository Link

GitHub Repository: [INSERT YOUR GITHUB REPOSITORY URL]

The repository contains:

Python source code.
Streamlit application.
Requirements file.
README documentation.
Test dataset.
Five saved classification models.
Model comparison results.


D. Models Used and Evaluation Metrics

Observations on Model Performance

1. Logistic Regression

Logistic Regression provides a baseline for binary classification. It models the relationship between customer attributes and subscription probability. Its performance can be evaluated using accuracy, AUC, and other classification metrics.

2. Decision Tree

The Decision Tree Classifier identifies patterns through a sequence of decision rules. It is easy to interpret but may overfit the training dataset.

3. K-Nearest Neighbors (KNN)

KNN classifies customers based on the nearest observations in the feature space. Its performance depends on the choice of K and appropriate feature scaling.

4. Gaussian Naive Bayes

Gaussian Naive Bayes uses probability distributions to predict the target class. It is computationally efficient but assumes conditional independence between features.

5. Support Vector Machine (SVM)

SVM attempts to find an optimal decision boundary between the two classes. It can perform well on complex classification problems, although training may require more computational time.

Overall Winner for the Dataset

The overall winning model will be selected after comparing the actual evaluation results.

The selection will consider:

Higher AUC Score.
Higher F1 Score.
Higher MCC Score.
Good accuracy and precision-recall balance.

Best Performing Model: [INSERT MODEL NAME AFTER RUNNING THE EXPERIMENT]

Conclusion: The five machine learning classification algorithms were implemented and evaluated on the Bank Marketing Dataset. Their performance was compared using six evaluation metrics. The experimental results help identify the most suitable classification algorithm for predicting customer term deposit subscriptions.
