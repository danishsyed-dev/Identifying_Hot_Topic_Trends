# Identifying Hot Topic Trends in Streaming Text Data

A Django-based web application that uses **Machine Learning** algorithms to identify and predict hot topic trends in streaming text data using **Sequential Evolution Model** based on **Distributed Representations**.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Django](https://img.shields.io/badge/Django-6.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Overview

This project implements a system for analyzing text data and predicting whether a topic is a "Hot Topic" or "Normal Topic" using various machine learning algorithms including:

- **Word2Vec** - For distributed word representations
- **Naive Bayes Classifier**
- **Support Vector Machine (SVM)**
- **Logistic Regression**
- **Decision Tree Classifier**
- **Gradient Boosting Classifier**

## 🔑 Keywords

`Distributed Representations` | `Sequential Evolution Model` | `Text Analysis` | `Word2Vec` | `Topic Trends` | `Knowledge Graph`

## 🛠️ Tech Stack

- **Backend:** Django 6.0, Python 3.13
- **Database:** SQLite3
- **ML Libraries:** Scikit-learn, Gensim (Word2Vec)
- **Frontend:** HTML, CSS, Bootstrap
- **Charts:** CanvasJS

## 📁 Project Structure

```
.
├── identifying_hot_topic_trends/    # Django settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── Remote_User/                     # User app
│   ├── models.py
│   └── views.py
├── Service_Provider/                # Admin app
│   ├── models.py
│   └── views.py
├── Template/
│   ├── htmls/                       # HTML templates
│   └── images/                      # Static files
├── manage.py                        # Django entry point
├── START_SERVER.bat                 # Windows quick start script
├── requirements.txt                 # Project dependencies
└── .gitignore                       # Git ignore file
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/danishsyed-dev/Identifying_Hot_Topic_Trends.git
cd Identifying_Hot_Topic_Trends
```

### Step 2: Create Virtual Environment (Recommended)
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Start the Server
```bash
python manage.py runserver
```

Or on Windows, simply double-click `START_SERVER.bat`

### Step 6: Access the Application
Open your browser and go to: `http://127.0.0.1:8000/`

## 👥 User Types

### Remote User
- Register and login
- Predict hot topic trends by entering text data
- View profile

### Service Provider (Admin)
- Login: `Admin` / `Admin`
- Train and test ML models
- View accuracy charts (Bar, Line)
- View all predictions and ratios
- Download predicted datasets
- Manage remote users

## 📊 Features

1. **User Registration & Authentication**
2. **Hot Topic Prediction** - Enter headline, description, and source to predict
3. **ML Model Training** - Train multiple classifiers on the dataset
4. **Accuracy Visualization** - View model performance in charts
5. **Data Export** - Download predictions as Excel files
6. **Prediction Analytics** - View ratio of Hot vs Normal topics

## 📈 Machine Learning Models

| Model | Description |
|-------|-------------|
| Naive Bayes | Probabilistic classifier based on Bayes' theorem |
| SVM | Linear Support Vector Classification |
| Logistic Regression | Binary classification using logistic function |
| Decision Tree | Tree-based classification algorithm |
| Gradient Boosting | Ensemble method using boosting technique |

## 🔧 Configuration

The main settings are in `identifying_hot_topic_trends/settings.py`:

- `DEBUG = True` (Set to `False` in production)
- `DATABASES` - SQLite3 configuration
- `STATIC_URL` - Static files URL
- `TEMPLATES` - Template directories

## 📝 License

This project is for educational purposes.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Contact

Your Name - SYED DANISH ALI
Email - knightdanish@outlook.com

Project Link: [https://github.com/danishsyed-dev/Identifying_Hot_Topic_Trends](https://github.com/danishsyed-dev/Identifying_Hot_Topic_Trends)

---
⭐ Star this repository if you found it helpful!
