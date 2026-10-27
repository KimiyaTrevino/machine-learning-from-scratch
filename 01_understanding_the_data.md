# Lesson 1: Understadning My Dataset
## What am I trying to learn?

Can sleep measurements help predict reported stress?
Before building a model, I need to understand what was measured,
what each row represents, and which columns are available.

## Where does the data come from?

The LEMURS study examined sleep and stress in college students.
The published analysis included 525 participants.

Wearable devices collected measurements, and participants
answered weekly surveys during October–December 2022.

Source study:
https://doi.org/10.1371/journal.pdig.0000473

Dataset:
https://plos.figshare.com/articles/dataset/Sleep_Measures_Data_/25587563

Credit: Bloomfield and colleagues, 2024.
Dataset license: CC BY 4.0.

## How does this connect to machine learning?

| Term | Meaning in this project |
|---|---|
| Example | One observation used for learning or testing |
| Feature/input (x) | Information given to the model, such as sleep duration |
| Target (y) | The measured stress outcome I want to predict |
| Prediction (ŷ) | The model’s estimate of that outcome |
| Error | The difference between the prediction and the measured outcome |

The target must come from the actual measurements.
I will not invent stress scores based on how long someone slept.

## What the paper examined

The study examined weekly relationships between reported stress
and wearable measurements, including sleep duration.

That does not automatically make this a next-day mood prediction
dataset. I need to check the timing and definitions in the files.

## Questions to answer when I open the data

- What are the column names?
- What does one row represent?
- Is there a participant ID?
- Is there a week or date column?
- How is sleep duration measured, and in what units?
- Is stress stored as a score, a category, or both?
- Are any values missing?
- Does the same participant appear in multiple rows?

## My findings

I have not inspected the downloaded file yet.

Column names:
Meaning of one row:
Sleep variable and units:
Stress variable and scale:
Questions I still have:

## Important distinction

A relationship between sleep and stress does not prove that
sleep causes stress or that stress causes sleep changes.

This project is for learning, not diagnosis or disease prediction.
