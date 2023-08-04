# **IPL Win Predictor**

![IPL](https://img.shields.io/badge/IPL-Win%20Predictor-orange)

The IPL Win Predictor is a data science and analytics project that aims to predict the probability of a team winning an IPL match based on the current match situation. It is an interactive web application developed using Python, Streamlit, and Plotly.

## **Project Overview**

The IPL Win Predictor project involves the following key steps:

1. **Data Source**: The project utilizes two datasets - 'deliveries.csv' and 'matches.csv' - containing detailed information about deliveries and matches played in various IPL seasons.

2. **Data Preprocessing**: Data preprocessing is carried out to clean, filter, and merge the datasets. The process includes merging the 'total_runs' data with the 'matches' DataFrame, handling matches with the Duckworth-Lewis (DL) method applied, and creating new features like 'current_score', 'runs_left', 'balls_left', and 'wickets'.

3. **Data Analysis**: Various data analysis techniques are employed to gain insights into the IPL matches. Exploratory data analysis (EDA) is performed to visualize match data, team performances, and other relevant trends.

4. **Model Building**: The heart of this project lies in building a predictive model. A logistic regression model is used to predict the probability of a team winning based on input features such as batting team, bowling team, city, runs left, balls left, wickets, current run rate (CRR), and required run rate (RRR).

5. **Model Evaluation**: The model's performance is evaluated using a test set and accuracy metrics. The accuracy score is used to assess how well the model predicts the outcomes of IPL matches.

6. **Web Application**: The IPL Win Predictor is converted into an interactive web application using Streamlit, a Python library for creating web apps. The web app allows users to select batting and bowling teams, city, target score, current score, overs completed, and wickets. The app then predicts the probability of each team winning the match based on the provided inputs.

## **Project Highlights**

- Developed an interactive web application to predict IPL match outcomes.
- Processed and cleaned data using Pandas and NumPy for data quality assurance.
- Utilized data visualization techniques to present insights in a user-friendly manner.
- Deployed the application on the Streamlit cloud platform for easy accessibility.

## **Business Impact**

- Provided actionable insights for decision-making in the context of IPL match predictions.
- Demonstrated proficiency in data analysis, visualization, and project management.

## **Conclusion**

The IPL Win Predictor project provides an engaging and interactive platform for IPL enthusiasts to explore match probabilities and make virtual predictions. It is a showcase of data analysis, model building, and web development skills of ***Rohit Verma***.

## **Contact Information**

- Name: Rohit Verma
- Location: Indore, India
- LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/rohitverma/)
- Email: rohitvermav0021@gmail.com

Feel free to interact with the web app and explore the exciting world of IPL match predictions!
