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

- **Backend:** Django 6.0, Python 3.10+
- **Database:** SQLite3
- **ML Libraries:** Scikit-learn, Gensim (Word2Vec)
- **Frontend:** HTML, CSS, Bootstrap
- **Charts:** CanvasJS

## 📁 Project Structure

```
.
├── identifying_hot_topic_trends/    # Django settings
│   ├── settings.py                  # Main configuration file
│   ├── urls.py                      # URL routing
│   └── wsgi.py                      # WSGI configuration
├── Remote_User/                     # User app
│   ├── models.py                    # Database models
│   ├── views.py                     # User views and prediction logic
│   └── migrations/                  # Database migrations
├── Service_Provider/                # Admin app
│   ├── models.py                    # Admin models
│   ├── views.py                     # Admin views and ML training
│   └── migrations/                  # Database migrations
├── Template/
│   ├── htmls/                       # HTML templates
│   └── images/                      # Static files
├── Datasets.csv                     # Sample training dataset (98 examples)
├── manage.py                        # Django entry point
├── setup_check.py                   # Setup validation script
├── START_SERVER.bat                 # Windows quick start script
├── run_server.py                    # Alternative server startup script
├── requirements.txt                 # Project dependencies
├── USAGE_GUIDE.md                   # Detailed usage instructions
└── .gitignore                       # Git ignore file
```

## 🚀 Installation & Setup

### TL;DR - Quick Start (For Experienced Users)
```bash
git clone https://github.com/danishsyed-dev/Identifying_Hot_Topic_Trends.git
cd Identifying_Hot_Topic_Trends
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
# Open http://127.0.0.1:8000/ in your browser
```

### Prerequisites
- Python 3.10 or higher (tested with Python 3.12)
- pip (Python package manager)
- Git

### Detailed Setup Guide

#### Step 0: Verify Setup (Optional but Recommended)
```bash
python setup_check.py
```
This will check if all dependencies are installed and the project is properly configured.

#### Step 1: Clone the Repository
```bash
git clone https://github.com/danishsyed-dev/Identifying_Hot_Topic_Trends.git
cd Identifying_Hot_Topic_Trends
```

#### Step 2: Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on Linux/Mac
source venv/bin/activate
```

#### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

#### Step 4: Initialize Database
```bash
# Run database migrations
python manage.py migrate
```

**Note:** The `makemigrations` command is not needed as migrations are already included.

#### Step 5: Start the Server
```bash
python manage.py runserver
```

**Alternative for Windows:** Double-click `START_SERVER.bat` (no admin privileges required)

**Alternative method:** Use the provided run script:
```bash
python run_server.py
```

#### Step 6: Access the Application
Open your browser and navigate to: **`http://127.0.0.1:8000/`**

**📖 First time using the app?** Check out the [Usage Guide](USAGE_GUIDE.md) for detailed instructions.

## 👥 User Types & Default Credentials

### Remote User
- **Registration Required:** Create an account to access user features
- Features:
  - Register and login
  - Predict hot topic trends by entering text data
  - View profile

### Service Provider (Admin)
- **Default Login Credentials:**
  - Username: `Admin`
  - Password: `Admin`
- Features:
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

## 📁 Dataset Information

The project includes a sample dataset (`Datasets.csv`) for training and prediction. The dataset contains:
- **Description:** Text descriptions of various topics
- **Label:** Binary classification (0 = Normal Topic, 1 = Hot Topic)

### Dataset Structure
```csv
Description,Label
"Breaking news: Major earthquake strikes...",1
"Local bakery opens new branch...",0
```

**Note:** The provided dataset is a sample. For production use, you should:
1. Expand the dataset with more diverse examples
2. Ensure balanced representation of both classes
3. Include domain-specific topics relevant to your use case

### Using Your Own Dataset
To use your own dataset:
1. Create a CSV file named `Datasets.csv` in the root directory
2. Ensure it has two columns: `Description` and `Label`
3. Label format: 0 = Normal Topic, 1 = Hot Topic
4. Save with UTF-8 or Latin-1 encoding

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

## 🐛 Troubleshooting

### Common Issues and Solutions

#### Issue: "Couldn't import Django"
**Solution:**
```bash
# Ensure Django is installed
pip install Django>=6.0

# Or reinstall all requirements
pip install -r requirements.txt
```

#### Issue: "No module named 'sklearn'"
**Solution:**
```bash
pip install scikit-learn>=1.0
```

#### Issue: "FileNotFoundError: Datasets.csv"
**Solution:**
- Ensure `Datasets.csv` exists in the root directory
- The repository includes a sample dataset
- If missing, create one following the dataset structure above

#### Issue: Database errors after pulling updates
**Solution:**
```bash
# Delete the database and reinitialize
rm db.sqlite3
python manage.py migrate
```

#### Issue: Port 8000 already in use
**Solution:**
```bash
# Use a different port
python manage.py runserver 8080

# Or find and kill the process using port 8000 (Unix/Linux)
lsof -ti:8000 | xargs kill -9

# Windows
netstat -ano | findstr :8000
taskkill /PID <PID_NUMBER> /F
```

#### Issue: Static files not loading
**Solution:**
```bash
# Collect static files
python manage.py collectstatic --noinput
```

#### Issue: START_SERVER.bat requires admin privileges (Windows)
**Solution:**
- Run the batch file as administrator, or
- Use `python manage.py runserver` instead

### Getting Help

If you encounter issues not listed here:
1. Check the Django error message in the console
2. Ensure all dependencies are installed: `pip list`
3. Verify Python version: `python --version` (should be 3.10+)
4. Check if migrations are applied: `python manage.py showmigrations`

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
