# Machine Learning From Scratch: Sleep and Stress

## About this project

I’m currently learning about neural networks and machine learning,
and I’m taking an AI in Medicine course.

I created this project to connect the math I’m learning with
hands-on Python practice. I want to understand how a model makes
predictions, learns from mistakes, and gets evaluated.

This repository documents my progress from the basics, including
my notes, calculations, code, questions, and mistakes.

## My research question

How well can sleep measurements predict a person’s reported
stress score?

I’m interested in sleep and psychological well-being. This project
will explore patterns in data without assuming that sleep alone
determines someone’s stress.

## Data source

The planned source is the publicly shared data accompanying:

“Predicting stress in first-year college students using sleep
data from wearable devices” (2024).

Study:
https://doi.org/10.1371/journal.pdig.0000473

Public dataset:
https://plos.figshare.com/articles/dataset/Sleep_Measures_Data_/25587563

Before modeling, I will inspect the released files, documentation,
usage terms, and available variables to confirm which question
the data can support.

No confidential research data or internal team materials will
be included in this repository.

## What the model will do

- Input: sleep measurements, starting with sleep duration.
- Target: the reported stress score, if available and appropriately
  matched to the sleep measurements.
- Output: a predicted stress score.

Stress is not the same as mood, happiness, or a medical diagnosis.

## Starting with the math

My first model will use:

predicted stress = weight × sleep duration + bias

The weight controls how the prediction changes with sleep duration.
The bias adds a constant to the prediction.

I will begin with a tiny fictional example to understand the
calculation. Then I will apply what I learn to suitable real data.

The relationship will be learned from examples rather than
assuming that a specific amount of sleep means a specific stress level.

## Project roadmap

- [x] Choose a topic: sleep and stress
- [x] Identify a candidate public study and dataset
- [ ] Inspect the dataset and confirm the prediction task
- [ ] Understand inputs, targets, weights, and bias
- [ ] Calculate a prediction by hand
- [ ] Write the prediction in Python
- [ ] Calculate prediction errors and mean squared error
- [ ] Learn gradients and gradient descent
- [ ] Write a training loop to update the weight and bias
- [ ] Prepare the real data and separate training and test participants
- [ ] Compare the model with a simple baseline
- [ ] Evaluate predictions on the held-out test data
- [ ] Create graphs and explain findings and limitations

## How I will evaluate the model

I will compare my model with a baseline that always predicts
the average stress score from the training data.

If participants have multiple records, I will keep each person's
records together when splitting training and test data.

This helps check whether the model works for people it has not
already seen during training.

## What I will document

For each lesson, I will include:

1. What I am trying to understand
2. An explanation in my own words
3. The math worked out step by step
4. Python code for the same calculation
5. Results and graphs
6. Mistakes, questions, and what I learned

## Limitations

This is an educational project, not a clinical prediction tool.

An association between sleep and stress does not prove that one
causes the other. Other factors may influence both.

This project will not estimate future disease risk because that
requires different data and validation.

## Current status

Project planning is complete. Dataset inspection and model
implementation are next. No model has been trained yet.
