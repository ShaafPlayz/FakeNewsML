# FakeNewsML

**FakeNewsML** is a machine learning-powered web application that detects fake news using natural language processing techniques. Built with Flask and scikit-learn, it provides real-time classification of news articles as genuine or fabricated.

## 📸 Screenshots

### HomePage
![image](https://github.com/user-attachments/assets/afe42b81-53a0-4f09-ac5b-45712b381072)

### Use Case
![image](https://github.com/user-attachments/assets/f990da5d-a581-4e04-a141-142b74ee8783)

## 🔍 Features

- **Real-time Detection**: Instantly classify news articles as fake or real
- **Machine Learning Model**: Uses PassiveAggressiveClassifier with TF-IDF vectorization
- **Responsive Web Interface**: Clean, modern UI built with HTML, CSS, and Tailwind CSS
- **High Accuracy**: Trained model with stratified sampling for balanced predictions
- **Interactive Dashboard**: Shows model accuracy and prediction confidence
- **Easy to Use**: Simple text input interface for quick analysis

## 🚀 How It Works

1. **Data Processing**: The model is trained on a comprehensive news dataset (`news.csv`)
2. **Feature Extraction**: Uses TF-IDF (Term Frequency-Inverse Document Frequency) to convert text into numerical features
3. **Classification**: PassiveAggressiveClassifier predicts whether the input text is fake or real news
4. **Real-time Prediction**: Users can input any news text and get instant classification results

## 🛠 Tech Stack

- **Backend**: Python 3.x, Flask
- **Machine Learning**: scikit-learn, numpy, pandas
- **Frontend**: HTML5, CSS3, Tailwind CSS
- **Development**: Jupyter Notebook for model development
- **Tools**: TF-IDF Vectorization, PassiveAggressiveClassifier

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ShaafPlayz/FakeNewsML.git
   cd FakeNewsML
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure you have the dataset:**
   - Make sure `news.csv` is in the project root directory
   - The dataset should contain 'text' and 'label' columns

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Open your browser:**
   - Navigate to `http://localhost:5000`
   - Start classifying news articles!

## 📊 Model Performance

- **Algorithm**: PassiveAggressiveClassifier
- **Feature Extraction**: TF-IDF with English stop words removal
- **Training Split**: 80% training, 20% testing (stratified sampling)
- **Accuracy**: Displayed on the homepage (typically >90%)

## 🔬 Development

### Jupyter Notebook
The project includes `fake_news.ipynb` for model development and experimentation:
- Data exploration and preprocessing
- Model training and evaluation
- Performance metrics and visualization

### Project Structure
```
FakeNewsML/
├── app.py                 # Main Flask application
├── fake_news.ipynb        # Jupyter notebook for model development
├── news.csv              # Training dataset
├── requirements.txt       # Python dependencies
├── templates/            # HTML templates
│   ├── home.html         # Homepage template
│   └── prediction.html   # Results page template
├── static/              # Static assets
│   └── src/             # CSS and styling
└── README.md            # Project documentation
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Future Enhancements

- [ ] Add more sophisticated NLP models (BERT, RoBERTa)
- [ ] Implement confidence scores for predictions
- [ ] Add batch processing for multiple articles
- [ ] Create API endpoints for programmatic access
- [ ] Add data visualization for model insights
- [ ] Implement user feedback system for model improvement

## 📧 Contact

Created by [ShaafPlayz](https://github.com/ShaafPlayz) - feel free to contact me!
