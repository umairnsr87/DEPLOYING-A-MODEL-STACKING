from flask import Flask, jsonify,request

from sklearn.externals import joblib

import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))
from nltk.stem.wordnet import WordNetLemmatizer
lemma = WordNetLemmatizer()

def split_into_lemmas(message):
    message=message.lower()
    words = word_tokenize(message)
    words_sans_stop=[]
    for word in words :
        if word in stop:continue
        words_sans_stop.append(word)
    return [lemma.lemmatize(word) for word in words_san

app = Flask(__name__)

@app.route('/',methods=['POST'])
def home():
    return 'Hello World'

@app.route('/predict', methods=['POST'])
def predict():
    json_ = request.get_json(silent=True)
    message=json_.get('message')
    mydf = pd.DataFrame({'message':message})
    print(mydf)
    prediction = clf.predict_proba(mydf['message'])
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    clf = joblib.load('/Users/umairansari/Dropbox/PDS V3/10. Stacking , pipelines and python model API/my_model_pipeline.pkl')
    app.run(port=5000)
    
#curl -H "Content-Type: application/json" -X POST -d '{"message":["I‘m going to try for 2 months ha ha only joking"]}' http://127.0.0.1:5000/predict
