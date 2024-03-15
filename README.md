# Valentine's Day App (Desktop GUI)
A Desktop GUI application using PySide6 on Valentine's Day data - A guide with codes to create your first desktop application. For the detailed guide, [check out this tutorial on Towards Data Science.](https://towardsdatascience.com/building-your-first-desktop-application-using-pyside6-a-data-scientist-edition-e2275cf0c977)

## Data

The National Retail Federation in the United States has been conducting surveys on how people plan to celebrate Valentine's Day for over a decade. The data provides a demographic breakdown of total spending, average spending, types of gifts planned and spending per type of gift. 

To get started please download the data, which is free to use, from [Kaggle](https://www.kaggle.com/datasets/joebeachcapital/valentines-day-consumer-data/data) and add it under 'data/' directory.
## Pre-requisites

The project was developed using Python 3.8.10 with the following packages.
- Pandas
- Matplotlib
- Pyside6

Installation with pip:

```bash
pip install -r requirements.txt
```
## Getting Started
Open the terminal in your machine and run the following command after cloning the repository with all data and files.
```bash
python3 valentines_app.py 
```
## Files
- valentines-analysis.ipynb : Jupyter Notebook with all the workings including analysis and visualizations.
- valentines_app.py: Script for the Desktop GUI application
- requirements.txt : pre-requisite libraries for the project
- data/ : the 3 CSV datasets for the project


## Summary
This project was aimed at building our first desktop application, from a data scientist's point-of-view. We start asking interesting questions from a dataset and create visualizations as answers for these questions. Then we wrap these visualizations, in the form of an interactive desktop GUI application such that on a press of the button, the visualizations appear on the application.

## Acknowledgements

[The National Retail Federation](https://nrf.com/research-insights/holiday-data-and-trends/valentines-day/valentines-day-data-center), for collecting, cleaning and providing the data for analysis.

[PySide6](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/index.html), for the open-source library for desktop GUI application development.


