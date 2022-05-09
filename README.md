# cs5293sp22-project3

## Name: Venkat Narra

## How to run the project
``` bash
pipenv run python project3.py
```
By running the above command in the compiler, it takes data from the root folder, unredacter.tsv file and performs ML on this data

## External libraries that are used in the project

1. **sckit-learn:**
    ```bash
    pipenv install scikit-learn
    ```
   - It's used for accessing the Machine learning model KNN classifier.
   - scores like f1_score, precision_score and recall_score can be easyly caluclate.
2. **Pandas:**
    ```bash
    pipenv install pandas
    ```
    - Used to create a data frame .

### Bugs
1. The predicted data is not accurate.
2. The model is predicting the names by the length of the names 

## Functions in this project

1. add_data():
    - This funtion add the addition coloumns to the data frame ,that are required for the taining and validation.
2. score_predictor():
    - This funtion takes the validation values and predicted data to caluclate f1_score, precision_score and recall_score.
