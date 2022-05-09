# cs5293sp22-project3

## Name: Venkat Narra

## How to run the project
- This below command is used to install all the necessory packages tha are required for this project .

``` bash
pipenv install
```
 - This below commmand is used run the project.
 
``` bash
pipenv run python project3.py
```
By running the above command in the compiler, it takes data from the root folder, unredacter.tsv file and performs ML on this data.
In this project ,I divided the data acoording to training, testing and validation. I used the training data to tarin the model and used the validation type data to predict the model.

## External libraries that are used in the project

1. **sckit-learn:**
    ```bash
    pipenv install scikit-learn
    ```
   - It's used for accessing the Machine learning model KNN classifier.
   - scores like f1_score, precision_score and recall_score can be easyly caluclate.
   - DictVectorizer is used to vectorize the list of dictnories.
2. **Pandas:**
    ```bash
    pipenv install pandas
    ```
    - Used to create a data frame and add the extra columns that are necessory to send into the DictVectorizer.
    - Created a each row with required variables to dictionary and vectorized the data

### Bugs
1. The predicted data is not accurate.
2. The model is predicting the names by the length of the names 

## Functions in this project

1. add_data():
    - This funtion add the addition coloumns to the data frame ,that are required for the taining and validation.
    - nam_len is the header that contain length of the name in that row is added to the data frame.
    - text_len is the header that contain length of he redated sentences length is added.
2. score_predictor():
    - This funtion takes the validation values and predicted data to caluclate f1_score, precision_score and recall_score.
    - It caluclates the required scores and return the list with the scores.

