# Employee Attrition Prediction Web App

An end-to-end Machine Learning web application that predicts whether an employee is likely to leave an organization using Logistic Regression, deployed with Flask.

This project demonstrates the complete machine learning workflow, including data preprocessing, model training, and web deployment.

--- 

## Project Overview 

Employee attrition is a critical challenge for organizations. This system predicts attrition risk based on employee attributes such as experience, age, job role match, promotion status, department, gender, and tenure.
  
The application provides a user-friendly web interface with probability-based predictions for informed decision-making.
  
---

## Machine Learning Details

* Algorithm: Logistic Regression
* Problem Type: Binary Classification (Stay / Leave)
* Number of Features: 23
* Target Variable: Stay/Left
* Output: Probability-based prediction
 
The model was trained without data leakage by excluding the target variable from the input features.

---

## Technology Stack

* Programming Language: Python
* Libraries: Pandas, NumPy, Scikit-learn
* Web Framework: Flask
* Frontend: HTML, CSS
* Model Persistence: Pickle

---

## Key Features

* End-to-end machine learning pipeline
* One-hot encoded categorical features
* Logistic Regression classifier
* Probability-based prediction output
* Flask web application
* Modular and clean project structure

---

## Project Structure

```
attrition_app/
│
├── app.py
├── model.pickle
├── processed table.csv
├── requirements.txt
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── README.md
```

---

## How to Run the Project Locally

### Step 1: Clone the repository

```bash
git clone 
cd employee-attrition-prediction
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the Flask application

```bash
python app.py
```

### Step 4: Open in a browser

```
http://127.0.0.1:5000
```

---

## Output Example

* Prediction: Not Likely to Leave
* Probability of Staying: 96.01 percent
* Probability of Leaving: 3.99 percent

These results support data-driven HR decisions.

---

## Use Cases

* Human resource analytics
* Employee retention strategy
* Machine learning portfolio project
* Educational reference for ML and Flask integration

---

## Future Enhancements

* Feature importance and model explainability
* UI improvements using Bootstrap
* Cloud deployment
* Authentication and role-based access

---

## Author

Noorullah Zamindar
Machine Learning and AI Engineer

LinkedIn: [https://www.linkedin.com/in/noorullah-zamindar-4975a328a/](https://www.linkedin.com/in/noorullah-zamindar-4975a328a/)
GitHub: [https://github.com/NoorullahZamindar-007](https://github.com/NoorullahZamindar-007)

---

## License

This project is provided for educational and demonstration purposes.

---

 
