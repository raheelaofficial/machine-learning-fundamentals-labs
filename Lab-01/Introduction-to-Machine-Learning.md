# Lab 01: Introduction to Machine Learning

## Objectives
By the end of this lab, students should be able to:
- Explain the basic machine learning workflow.
- Load and inspect a dataset using Python.
- Separate features and target labels.
- Train a simple classification model.
- Evaluate model performance.

## Tools
- Python
- Jupyter Notebook or Kaggle Notebooks
- Pandas
- Scikit-learn

## Practical Task: Iris Flower Classification

### Task 1: Load the dataset

Load the Iris dataset using Scikit-learn and display:
- Number of samples and features
- Feature names
- Class names
- First five rows

### Task 2: Prepare the data

Separate the input features (X) from the target labels (y). Split the data into training and testing sets using an 80:20 ratio.

### Task 3: Train a model

Train a K-Nearest Neighbors (KNN) classifier using k = 3.

### Task 4: Evaluate the model

Calculate and explain:
- Accuracy
- Confusion matrix
- Precision
- Recall
- F1-score

### Task 5: Industry-style investigation

Repeat the experiment with k = 1, 5, and 7.

Record the results in a table and explain why the choice of k affects model performance.

## Submission Requirements
Submit your notebook, results table, and a short explanation of your findings.

## Reflection Questions
1. Why do we split data into training and testing sets?
2. What happens when k is too small?
3. Is accuracy sufficient to evaluate every classification problem?
4. What additional tests would you perform before using this model in a real application?
