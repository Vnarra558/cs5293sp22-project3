import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
from textblob import TextBlob
import warnings
warnings.filterwarnings('ignore')

#Read the latest data file 
data=pd.read_csv('unredactor.tsv',sep='\\t',on_bad_lines='skip')
df=pd.DataFrame(data)


df.rename(columns={'cegme': 'gitid','training':'type', 'ashton kutcher': 'r_names','I couldn\'t image ██████████████ in a serious role, but his performance truly':'r_text'}, inplace=True)


def add_data(df):
    length=df['r_names'].map(lambda x: len(str(x)))
    df['name_len']=length
    t_length=df['r_text'].map(lambda x: len(str(x)))
    df['text_len']=t_length
    return df
def score_predictor(y_validation, pred_d):
    pre =precision_score(y_validation, pred_d, average= "weighted")
    f1 =f1_score(y_validation, pred_d, average= "weighted")
    recall =recall_score(y_validation, pred_d, average= "weighted")
    l=[pre,f1,recall]
    return l

df=add_data(df) 

# Seperating data for traing and validation
training_d=df[(df['type']=='training')]
testing_d=df[(df['type']=='testing')] 
validation_d=df[(df['type']=='validation')]

# Useing vectorizer to genrate features
dict_vectorizer = DictVectorizer()
f=training_d.filter(['r_names','name_len','r_text'], axis=1)
y_train=training_d['r_names']
dic_train=f.to_dict(orient='records')
train_features=dict_vectorizer.fit_transform(dic_train).toarray()

n=validation_d.filter(['name_len',], axis=1)
dic_valid=n.to_dict(orient='records')
validation_features=dict_vectorizer.transform(dic_valid).toarray()
y_validation=validation_d['r_names']


knn = KNeighborsClassifier()
knn.fit(train_features, y_train)
pred_d=knn.predict(validation_features)


accuracy=knn.score(validation_features,y_validation)


#caluclating the Precision_score,f1_score, and recall_score
p = score_predictor(y_validation, pred_d)
print("precision:",p[0])
print("F1_score:",p[1])
print("recall:",p[2])
