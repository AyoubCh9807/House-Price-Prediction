# 🏡 House Price Prediction App

A desktop application built with **PySide6** that predicts house prices based on user input using **Linear Regression (scikit-learn)**. The app takes house features like **space (sqft)**, **number of bedrooms**, and **age (years)**, trains a model with your data, and predicts the price of a new house based on those features. It also **visualizes the results using Matplotlib**.

## 🧠 Features

- Input multiple house listings and their features
- Predict price of a new house based on 3 features
- View actual data points and prediction line on a graph
- Error handling for invalid inputs (e.g. negative numbers, empty fields)
- Simple and intuitive GUI

---

## 🛠 Tech Stack

- **Python 3.10+**
- **PySide6** – GUI development
- **scikit-learn** – Linear regression model
- **NumPy** – Data preparation
- **Matplotlib** – Graph plotting

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python and these packages installed:

pip install PySide6 scikit-learn matplotlib numpy

🏗 App Structure
-Input Section: Enter 5 sample house listings (space, bedrooms, age, price).

-Prediction Section: Enter the space, bedroom count, and age of the house to predict.

-Button: Click Predict House Price to visualize the data and prediction.

-Graph Output: Scatter plot of data points + regression line + predicted price.

📊 Machine Learning Explanation
I use Multiple Linear Regression to fit a model to the given house data. The model learns a relationship:
Price = a*space + b*bedrooms + c*age + intercept

Then it uses that equation to predict the price of a new house based on user-entered features.

💡 Example Data
Space (sqft)	Bedrooms	Age (years)	Price ($K)
1500	3	20	400
2000	4	10	500
3500	5	5	750
7500	10	30	900
1000	2	30	250

✅ What I Learned

-Building GUIs with PySide6

-Collecting and validating user input

-Visualizing data and regression lines using Matplotlib

-Applying scikit-learn's LinearRegression model

-Connecting all parts into a working desktop app

📂 Future Improvements

-Load/save data from CSV or JSON

-Add error bars or confidence intervals

-Allow custom number of entries

-Add styling and responsiveness to the GUI

📃 License
This project is for learning purposes. Feel free to fork, modify, and experiment!

🙋‍♂️ Author
Made with ❤️ by a first-year CS student exploring machine learning and GUI apps.
