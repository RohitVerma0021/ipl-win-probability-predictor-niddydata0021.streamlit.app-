import streamlit as st
import pickle
import pandas as pd
import time


st.set_page_config(page_title="Hello My name is rohit verma this is application was built by me",  layout='wide')
def predict_win():
    # page_bg_img = """
    # <style>
    # [data-testid="stAppViewContainer"]{
    # background-image: url("");
    # background-size: cover;
    # }
    # </style>
    # """
    # st.markdown(page_bg_img, unsafe_allow_html=True)

    teams= ['Chennai Super Kings',
     'Dehli Capitals',
     'Gujarat Lions',
     'Kolkata Knight Riders',
     'Mumbai Indians',
     'Kings XI Punjab',
     'Rajasthan Royals',
     'Royal Challengers Bangalore',
     'Sunrisers Hyderabad']

    cities = ['Hyderabad', 'Rajkot', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata',
           'Delhi', 'Chandigarh', 'Kanpur', 'Jaipur', 'Chennai', 'Cape Town',
           'Port Elizabeth', 'Durban', 'Centurion', 'East London',
           'Johannesburg', 'Kimberley', 'Bloemfontein',
           'Cuttack', 'Nagpur', 'Dharamsala', 'Visakhapatnam', 'Pune',
           'Raipur', 'Ranchi', 'Sharjah','Mohali',
           'Bengaluru']

    ## this  is style
    # st.info('This is a purely informational message', icon="ℹ️")
    st.info("Disclaimer: This app is for informational purposes only. The predictions generated are not guaranteed to be accurate and should not be considered as professional advice for betting or any other purpose.", icon="⚠️")

    #-----------------------button style and show message when some one select click on the button-------------------------------------
    def cook_breakfast():
        msg = st.info('Gathering ingredients...')
        time.sleep(2)
        msg.empty()

        st.warning('This app only shows the probability based on the current situation. It is not a real prediction.')
        time.sleep(3)

        st.info('Predictions are for entertainment purposes only. Enjoy your virtual match! 🏏')

    ##############################################################
    pipe = pickle.load(open('pipe (1).pkl','rb'))
    col0,col10=st.columns(2)
    with col0:
        st.write('# IPL Win Predictor by 👉🏻')
        st.markdown('<span style="color:orange">you can reach me at ***rohitverma0021@gmail.com*** If you know more about this project to go on the Project_info page.</span>', unsafe_allow_html=True)
    with col10:
        st.image("img.png")

    col1,col2=st.columns(2)
    with col1:
        batting_team=st.selectbox("Select the batting team",sorted(teams))
    with col2:
        bolling_team=st.selectbox("Select the bowling team",sorted(teams))

    select_cities=st.selectbox("Select Host City",sorted(cities))
    target=st.number_input("Enter Target")
    col3,col4,col5=st.columns(3)
    with col3:
        score=st.number_input("Enter score")
    with col4:
        overs=st.number_input("Overs Completed")
    with col5:
        wickets=st.number_input("Wicket Out")
    if st.button("Predict Probability"):
        st.balloons()
        cook_breakfast()
        runs_left=target-score
        balls_left=120 - (overs*6)
        wickets = 10 - wickets
        crr = score/overs
        rrr = (runs_left*6)/balls_left
        input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bolling_team],'city':[select_cities],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})

        result = pipe.predict_proba(input_df)
        #st.text(result)
        loss = result[0][0]
        win = result[0][1]
        st.header(batting_team + "- " + str(round(win*100)) + "%")
        st.header(bolling_team + "- " + str(round(loss*100)) + "%")


def info():
    st.title("IPL Win Predictor - Project Overview")
    st.markdown('<p style="color: #FFA500; font-size: 24px;"><b>Hello, recruiters! My name is Rohit Verma, and I am a Data Science and Analytics professional with a strong academic background and a passion for data-driven decision-making.</b></p>', unsafe_allow_html=True)
    st.markdown("<h3 style='color: red;'>Project Overview</h3>", unsafe_allow_html=True)
    st.write(
        "<span style='color: orange;'>This IPL Win Predictor project is a data science and analytics application developed by Rohit Verma. The goal of this project is to predict the probability of a team winning an IPL match based on the current match situation.</span>",
        unsafe_allow_html=True
    )
    st.markdown("<h3 style='color: red;'>Data Source</h3>", unsafe_allow_html=True)
    st.write(
        "The project uses two datasets - 'deliveries.csv' and 'matches.csv'. These datasets contain detailed information about deliveries and matches played in various IPL seasons."
    )

    st.markdown("<h3 style='color: red;'>Data Preprocessing</h3>", unsafe_allow_html=True)
    st.write(
        "The project starts with data preprocessing to clean, filter, and merge the datasets. The key preprocessing steps include:"
    )
    st.write("- Merging the 'total_runs' data with the 'matches' DataFrame.")
    st.write("- Filtering the DataFrame to include matches of specific IPL teams.")
    st.write("- Handling matches with the Duckworth-Lewis (DL) method applied.")
    st.write("- Creating new features like 'current_score', 'runs_left', 'balls_left', and 'wickets'.")

    st.markdown("<h3 style='color: red;'>Data Analysis</h3>", unsafe_allow_html=True)
    st.write(
        "After preprocessing the data, various data analysis techniques are used to gain insights into the IPL matches. Exploratory data analysis (EDA) is performed to visualize match data, team performances, and other relevant trends."
    )

    st.markdown("<h3 style='color: red;'>Model Building</h3>", unsafe_allow_html=True)
    st.write(
        "The heart of this project lies in building a predictive model. The project uses a logistic regression model to predict the probability of a team winning based on the input features such as batting team, bowling team, city, runs left, balls left, wickets, current run rate (CRR), and required run rate (RRR)."
    )

    st.markdown("<h3 style='color: red;'>Model Evaluation</h3>", unsafe_allow_html=True)
    st.write(
        "The model's performance is evaluated using a test set and accuracy metrics. The accuracy score is used to assess how well the model predicts the outcomes of IPL matches."
    )

    st.markdown("<h3 style='color: red;'>Web Application</h3>", unsafe_allow_html=True)
    st.write(
        "The IPL Win Predictor is converted into an interactive web application using Streamlit, a Python library for creating web apps. The web app allows users to select batting and bowling teams, city, target score, current score, overs completed, and wickets. The app then predicts the probability of each team winning the match based on the provided inputs."
    )
    st.write("<h3 style='color: red;'>Project Highlights</h3>", unsafe_allow_html=True)
    st.write(
        "- Processed and cleaned data using Pandas and NumPy for <span style='color: white;'>data quality assurance</span>."
    )
    st.write(
        "- Utilized data visualization techniques to present insights in a <span style='color: white;'>user-friendly</span> manner."
    )
    st.write(
        "- Deployed the application on the Streamlit cloud platform for <span style='color: white;'>easy accessibility</span>."
    )

    st.write("<h3 style='color: red;'>Business Impact</h3>", unsafe_allow_html=True)
    st.write(
        "- Provided actionable insights for <span style='color: white;'>decision-making</span> in the context of IPL match predictions."
    )
    st.write(
        "- Demonstrated proficiency in <span style='color: white;'>data analysis</span>, <span style='color: white;'>visualization</span>, and <span style='color: white;'>project management</span>."
    )

    st.write("<h3 style='color: red;'>Conclusion</h3>", unsafe_allow_html=True)
    st.write(
        "The IPL Win Predictor project provides an engaging and interactive platform for IPL enthusiasts to explore match probabilities and make virtual predictions. It is a showcase of data analysis, model building, and web development skills of <span style='color: white;'>Rohit Verma</span>."
    )

    st.write("<h3 style='color: red;'>Contact Information</h3>", unsafe_allow_html=True)
    st.write("### ***[Rohit Verma](https://www.linkedin.com/in/rohit-verma-3094b8224/)***")
    st.write("Location: Indore, India")
    st.write(
        "Follow Me on LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/rohit-verma-3094b8224/)"
    )
    st.write("Email: <span style='color: white;'>rohitvermav0021@gmail.com</span>", unsafe_allow_html=True)
    st.write('Follow Me on GitHub: [GitHub](https://github.com/RohitVerma0021)')
    st.markdown(
        "Feel free to interact with the web app and explore the exciting world of IPL match predictions!",
        unsafe_allow_html=True
    )
selected_page = st.sidebar.radio("Navigation", ("Predict Win","Project Info"))

# Display the selected page content
if selected_page == "Project Info":
    info()
elif selected_page == "Predict Win":
    predict_win()


