# 📖 Usage Guide - Identifying Hot Topic Trends

This guide will walk you through using the application after installation.

## Table of Contents
1. [Starting the Application](#starting-the-application)
2. [Admin/Service Provider Workflow](#adminservice-provider-workflow)
3. [Remote User Workflow](#remote-user-workflow)
4. [Understanding the Results](#understanding-the-results)

## Starting the Application

### Method 1: Command Line
```bash
python manage.py runserver
```

### Method 2: Windows Batch File
Double-click `START_SERVER.bat`

### Method 3: Run Server Script
```bash
python run_server.py
```

Once started, open your browser and navigate to: **http://127.0.0.1:8000/**

## Admin/Service Provider Workflow

The Admin panel provides access to ML model training, analytics, and user management.

### 1. Login
- Navigate to: http://127.0.0.1:8000/
- Click on "Service Provider" or "Admin" login
- **Username:** `Admin`
- **Password:** `Admin`

### 2. Train Machine Learning Models

**Why train models first?**
Before making predictions, the system needs to learn from the dataset.

**Steps:**
1. From the admin dashboard, click **"Train Model"**
2. The system will train 5 different ML algorithms:
   - Naive Bayes
   - Support Vector Machine (SVM)
   - Logistic Regression
   - Decision Tree Classifier
   - Gradient Boosting Classifier
3. Wait for training to complete (usually takes 10-30 seconds)
4. You'll see accuracy scores for each model

**Expected Results:**
- Models typically achieve 85-95% accuracy on the sample dataset
- Each algorithm shows its classification accuracy

### 3. View Model Performance

**View Accuracy Charts:**
1. Click **"View Detection Accuracy"**
2. Choose chart type:
   - **Bar Chart** - Compare model accuracies side by side
   - **Line Chart** - See accuracy trends
3. Charts help you understand which ML model performs best

### 4. Manage Remote Users
- Click **"View Remote Users"**
- See all registered users
- View user details (username, email, location)

### 5. View All Predictions
- Click **"View Predicted Hot Topic Trends"**
- See all predictions made by remote users
- Each prediction shows:
  - Date of prediction
  - Headline
  - Description
  - Source
  - Classification (Hot Topic or Normal Topic)

### 6. View Prediction Statistics
- Click **"View Hot Topic Trends Ratio"**
- See pie charts showing:
  - Percentage of Hot Topics vs Normal Topics
  - Overall trend distribution

### 7. Download Prediction Data
- Click **"Download Trained DataSets"**
- Downloads an Excel file (.xls) containing all predictions
- Useful for further analysis or reporting

## Remote User Workflow

Remote users can register, login, and make predictions about whether topics are trending.

### 1. Register an Account

**First-time users must register:**
1. Click **"Remote User"** from the homepage
2. Click **"Register"**
3. Fill in the registration form:
   - Username
   - Email
   - Password
   - Phone Number
   - Country
   - State
   - City
4. Click **"Register"**
5. You'll be redirected to the login page

### 2. Login
1. Enter your registered username and password
2. Click **"Login"**
3. You'll be taken to your dashboard

### 3. Make a Prediction

**To predict if a topic is "Hot" or "Normal":**

1. Click **"Predict Hot Topic Trends"**
2. Fill in the prediction form:
   - **Serial Number:** Any identifier (e.g., "1", "Test-1")
   - **Date:** Prediction date (e.g., "2026-01-03")
   - **Headline:** Brief title of the topic
   - **Description:** Detailed description (this is what the ML model analyzes)
   - **Source:** Where the topic came from (e.g., "Twitter", "News")
3. Click **"Predict"**
4. Wait a few seconds for the ML models to analyze
5. See the result: **"Hot Topic"** or **"Normal Topic"**

**Example Input:**
- **Headline:** Breaking Economic News
- **Description:** Major stock market crash affects global economy with widespread panic selling
- **Source:** Financial Times
- **Expected Result:** Hot Topic

**Another Example:**
- **Headline:** Local Event Announcement
- **Description:** Community library announces extended weekend hours
- **Source:** Local Newsletter
- **Expected Result:** Normal Topic

### 4. View Your Profile
- Click **"View Profile"**
- See your registration details
- Update information if needed

## Understanding the Results

### What is a "Hot Topic"?
A **Hot Topic** is content that is:
- Breaking news or urgent information
- Likely to generate significant public interest
- Related to major events (disasters, political changes, economic crises)
- Has high impact or widespread relevance

**Examples of Hot Topics:**
- Natural disasters
- Political scandals
- Major economic changes
- International conflicts
- Breakthrough scientific discoveries
- Public health emergencies

### What is a "Normal Topic"?
A **Normal Topic** is content that is:
- Routine or everyday information
- Local or community-level news
- Scheduled or planned events
- Low urgency or impact

**Examples of Normal Topics:**
- Local business openings
- Community events
- Routine announcements
- Small-scale activities
- Administrative updates

### How the Prediction Works

The system uses an **ensemble of 5 ML models**:
1. Each model independently analyzes the description text
2. Models look for patterns learned from the training dataset
3. They vote on the classification
4. The final prediction is based on the majority vote

**Key Factors Analyzed:**
- Word choice and vocabulary
- Urgency indicators
- Impact keywords
- Context and tone
- Semantic patterns

### Improving Prediction Accuracy

For better predictions:
1. **Provide detailed descriptions** - More text gives models more data
2. **Use natural language** - Write as you would normally
3. **Include context** - Add relevant details
4. **Be specific** - Vague descriptions may lead to uncertain results

### Interpreting Accuracy Scores

When viewing model performance:
- **90-100%:** Excellent accuracy
- **80-90%:** Good accuracy
- **70-80%:** Moderate accuracy
- **Below 70%:** May need more training data

**Note:** The sample dataset is small (98 examples). For production use, a larger dataset (1000+ examples) is recommended.

## Tips and Best Practices

### For Administrators
1. **Train models first** before remote users make predictions
2. **Regularly check accuracy** to ensure models are performing well
3. **Download prediction data** periodically for backup
4. **Monitor prediction ratios** to understand trend patterns

### For Remote Users
1. **Provide meaningful descriptions** - The ML model analyzes the description field
2. **Test with known examples** - Try obvious hot topics and normal topics to understand the system
3. **Be patient** - Prediction takes 5-10 seconds as multiple models analyze the text

## Troubleshooting

### "Models not trained" error
- Admin must train models first
- Go to Admin panel → Train Model

### Prediction takes too long
- Normal for first prediction (models loading)
- Should be faster on subsequent predictions
- Check server logs for errors

### Low accuracy scores
- May need more training data
- Consider expanding Datasets.csv
- Ensure balanced examples (50% hot, 50% normal)

## Need More Help?

- Check the main README.md for installation issues
- Run `python setup_check.py` to verify setup
- Review server logs for error messages
- Check that Datasets.csv exists and is properly formatted

---

**Happy Predicting! 🚀**
