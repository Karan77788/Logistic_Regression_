# Logistic_Regression_
# Bank Term Deposit Subscription Predictor
A simple web app built with Flask and Logistic Regression to predict whether a customer will subscribe to a term deposit based on attributes like age, job, marital status, balance, and call duration.

#  Dataset
```
Features Used:

age: Age of the client

job: Type of job (admin, technician, blue-collar, etc.)

marital: Marital status

balance: Account balance

duration: Last contact duration

subscribed: Target variable (yes/no)
```
# How it Works
```
User inputs customer details through a web form.

The trained Logistic Regression model makes a prediction.

App returns whether the customer is likely to subscribe ("Yes" or "No").
```
# Technologies Used
```
Python 3

Flask

pandas

scikit-learn

HTML + CSS (basic styling)
```
 How to Run Locally
 1. Clone the repo or download files
 ```
git clone https://github.com/yourusername/bank-term-predictor.git
cd bank-term-predictor
```
 2. Install dependencies
```
pip install -r requirements.txt
```
 3. Train the model
```
python model.py
```
 4. Start the Flask app
```
python app.py
```
# Project Structure
```
bank_marketing_logreg_project/
├── app.py               # Flask web app
├── model.py             # Model training script
├── bank_data.csv        # Sample dataset (30 records)
├── logreg_model.pkl     # Saved trained model
├── requirements.txt     # Python dependencies
├── templates/
│   ├── index.html       # Input form
│   └── result.html      # Output page
├── static/
│   └── style.css        # CSS styling
└── README.md            # Project documentation
```
# Example Prediction
```
Input:
Age: 45
Job: technician
Marital Status: single
Balance: 2000
Duration: 200
```
```
Output:
Prediction: Yes ✅
```
# ScreenShots
![alt text](<Screenshot 2025-08-03 143105.png>)
![alt text](<Screenshot 2025-08-03 143123.png>)
![alt text](<Screenshot 2025-08-03 143132.png>)
