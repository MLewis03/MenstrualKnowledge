# MenstrualKnowledge

For my team's Spring 2024 Senior Capstone project, we conducted a survey among UNC Charlotte students about menstrual cycles.

This streamlit app presents the quiz portion to users, displays their score, and shows the correct answers along with the distrbutions by sex of sample used for the capstone project. 

The data was already precleaned as part of that project and so no preprocessing was neccesary here.

I made two tabs: one for the quiz and one for the answers. The answers tab only populates after the quiz has been submitted.

For the quiz, I used st.form() with radio buttons for each question used in the project survey.

At the end, balloons fly up, the score is displayed, and a notification pops up on the side that the user may view the answers tab now.

On the answers tab, for each question, the question is displayed followed by the correct answer, the source cited in the capstone paper, and a histogram of responses from the capstone sample.

Here is the link to the completed streamlit app: https://mlewis03-menstrualknowledge-app-cwns0f.streamlit.app/ 