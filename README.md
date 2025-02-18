# Depression Detection System

## 📌 Overview
This is a Flask-based web application that uses a Decision Tree model to classify tweets into three sentiment categories: **Positive, Neutral, and Negative**. The system is designed to analyze social media text data and determine whether a tweet expresses signs of depression.

## ✨ Features
✅ Load and preprocess tweet data from a text file and corresponding sentiment labels from an Excel file.  
✅ Train a **Decision Tree** model using `scikit-learn`.  
✅ Provide a **web interface** for users to input tweets and receive sentiment predictions.  
✅ Handle errors in **JSON decoding** and missing data gracefully.  

## 🛠 Technologies Used
- 🐍 **Python**
- 🔥 **Flask**
- 🧠 **scikit-learn**
- 📊 **pandas**
- 📜 **json**
- 🔤 **CountVectorizer** (for text feature extraction)
- 🎨 **HTML & CSS** (for the frontend UI)

## 🚀 Installation
1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-repo/depression-detection.git
   cd depression-detection
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Ensure you have the necessary data files:**
   - `processed_data/output.xlsx` (contains sentiment labels)
   - `data/tweetdata.txt` (contains raw tweet data in JSON format)

## ▶️ Usage
1. **Run the application:**
   ```sh
   python app.py
   ```
2. **Open your browser and go to:**
   ```
   http://127.0.0.1:5000/
   ```
3. **Enter a tweet** in the input field and submit to get a sentiment prediction.

## 📁 Project Structure
```
📂 depression-detection/
├── 📂 data/
│   ├── 📄 tweetdata.txt  # Raw tweet data in JSON format
├── 📂 processed_data/
│   ├── 📄 output.xlsx    # Processed sentiment labels
├── 📂 templates/
│   ├── 🎨 index.html     # Web interface
├── 📝 app.py             # Flask application
├── 📜 requirements.txt   # Python dependencies
├── 📖 README.md          # Project documentation
```

## 🔗 API Endpoints
### `GET /`
- Renders the main web interface.

### `POST /predict`
- Accepts user input (tweet text) and returns a sentiment prediction.

## 🏗 Model Training Process
1. Load tweets from `data/tweetdata.txt`.
2. Load corresponding sentiment labels from `processed_data/output.xlsx`.
3. Preprocess text data using `CountVectorizer` (removing stopwords and converting text into a feature matrix).
4. Train a Decision Tree model using `sklearn.tree.DecisionTreeClassifier`.
5. Use the trained model to classify user input.

## ⚠️ Notes
- Ensure that the dataset is properly formatted to avoid JSON decoding errors.
- The system classifies tweets into three categories:
  - ✅ **1**: Positive
  - ⚪ **0**: Neutral
  - ❌ **-1**: Negative

## 🤝 Contributing
Feel free to fork this repository and submit pull requests with improvements or bug fixes.

## 📜 License
This project is open-source and available under the **MIT License**.

