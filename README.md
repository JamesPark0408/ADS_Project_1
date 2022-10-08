# MAST30034 Project 1 README.md
- Name: Park Chang Whan
- Student ID: 1129623

**Research Goal:** My research goal is predicting fares and proportion of rrips for green taxis in NYC

**Timeline:** The timeline for the research area is 1st July 2021 to 30th April 2022.

To run the pipeline, please visit the `scripts` directory and run the files in order:
1. `download.py`: This downloads the raw data into the `data/raw` directory.
2. `Preprocessing.ipynb`: This notebook details all preprocessing steps and outputs it to the `data/curated` directory.
3. `Feature_Selection.ipynb`: This notebook details feature selection process and splits data into train/test(predict) data. 
4. `Preliminary_Analysis.ipynb`: This notebook goes into detail feature analysis for chosen features for analysis and outputs necessary plots to the `plots` directory.
5. `Linear_Regression_Average_Fare.ipynb` and `Linear_Regression_log_prop_trips.ipynb`: These notebooks used to create, run and analyze models 

### Things to Take Note:
External Datasets (Weather.csv and taxi_zone files) were added manually as could not be directly downloaded by script.
Chloropeth map plots and external image (station_contributions.png) were manually added as well.
