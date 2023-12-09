# PowerPulse-Forecast
Machine Learning based electricity price forecasting model

![image](https://github.com/JohnLocke117/Electricity-Price-Forecasting/assets/99555479/992016fc-5e1c-4cee-8531-b76d87b0f7e2)

<p>
Our project is committed to advancing energy market intelligence in New Zealand 
through the deployment of cutting-edge machine learning and deep learning models. 
Through extensive model comparisons, we have determined that LSTM (Long Short-Term 
Memory) networks outperform other methods for electricity price prediction. As a 
result, we've exclusively adopted LSTM models to provide you with the most accurate 
and dependable electricity price forecasts.
</p>

## Dataset:
The data is collected from ENTSOE, a public portal, which contains 4 years of electrical consumption, 
generation, pricing, and weather data for New Zealand. 
website. The data is collected for 21 features like the following:

- time
- generation biomass
- generation fossil brown coal/lignite
- generation fossil coal-derived gas	
- generation fossil gas	
- generation fossil hard coal	
- generation fossil oil	
- generation fossil oil shale	
- generation fossil peat	
- generation geothermal


## Exploratory Data Analysis and Feature Selection:
We have performed the following EDA and Feature Selection techniques on the dataset:

- Pearson's Correlation
- Wrapper Method (Backward Elimination)
- LASSO (L1 Regularization)
- PCA (Principal Component Analysis)

## Machine Learning Models:
We have implemented the following Machine Learning Models on the dataset:

- Multiple Linear Regression
- LEAR (Multiple Linear Regression with LASSO)
- Random Forest Regressor
- XGBoost
- LSTMs

## How To Run:
The project is divided into 2 parts:
- Machine Learning Jupyter Notebook <br/>
The dataset and the complete code has been provided in the folder.
To run the code, simply execute the .ipynb file. 
Make sure the path of the dataset is entered correctly.
Use `pip install` to install any missing dependencies.


- Web Application <br/>
The Front-End Web App is designed by HTML/CSS and the backend has been designed by Flask.
To run the web app, simply execute the app.py file.
Make sure to have `flask` installed in your system.
