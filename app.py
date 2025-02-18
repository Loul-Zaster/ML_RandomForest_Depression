from flask import Flask, request, render_template
from sklearn import tree
import pandas as pd
import json
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)

# Load data and train the model once at the start
tweets_data = []
x = []
y = []
vectorizer = CountVectorizer(stop_words='english')

# Function to load the data
def load_data():
    sent = pd.read_excel('processed_data/output.xlsx')
    tweets_data_path = 'data/tweetdata.txt'
    
    with open(tweets_data_path, 'r', encoding='utf-8') as tweets_file:
     for line in tweets_file:
        line = line.strip()  # Xóa các ký tự trắng ở đầu và cuối dòng
        if not line:  # Nếu dòng trống, bỏ qua
            continue
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e} in line: {line}")  # Thông báo lỗi chi tiết nếu có dòng bị lỗi


    for i in range(len(tweets_data)):
        if tweets_data[i]['id'] == sent['id'][i]:
            x.append(tweets_data[i]['text'])
            y.append(sent['sentiment'][i])

# Train the decision tree model
def train_model():
    train_features = vectorizer.fit_transform(x)
    dtree = tree.DecisionTreeClassifier()
    dtree.fit(train_features, [int(r) for r in y])
    return dtree

# Load data and train the model once
load_data()
model = train_model()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_tweet = request.form['tweet']
    input_features = vectorizer.transform([input_tweet])
    prediction = model.predict(input_features)
    
    if prediction == 1:
        result = "Positive"
    elif prediction == 0:
        result = "Neutral"
    elif prediction == -1:
        result = "Negative"
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

