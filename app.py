import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(layout="wide")

st.title('Menstrual Knowledge Quiz')

df = pd.read_csv("Survey_Responses_Cleaned - Sheet1.csv")

df = df[df['UNCC_Affiliation'] != 'Alumni']

answers  = {
    'Cycle_Length': "28 days",
    'Fertile_Window_Timing': "A few days before ovulation",
    'Fertile_Days': "Six Days",
    'Cycle_Phases_Order': "Menstruation, Follicular Phase, Ovulation, Luteal Phase",
    'Ovulation_Dominant_Hormone': "Luteinizing hormone",
    'Blood_Loss': "Quarter cup"
}

for column, correct_answer in answers.items():
    df[f'{column}_score'] = df[column].apply(lambda x: 1 if str(x).strip().lower() == correct_answer.lower() else 0)

df['Total_Knowledge_Score'] = df.filter(like='_score').sum(axis=1)

df = df[['Sex', "Cycle_Length", "Fertile_Window_Timing", "Fertile_Days", "Cycle_Phases_Order", "Ovulation_Dominant_Hormone", "Blood_Loss", "Total_Knowledge_Score"]]

with st.form("my_form"):
   st.write("Test Your Knowledge of Menstrual Cycles!")
   selected_sex = st.radio('Are you male or female? ', ['Male',
                                                        'Female'])
   selected_length = st.radio('Approximately how long is a normal menstrual cycle? ', ['20 Days',
                                                                                       '28 Days', 
                                                                                       '36 Days'])
   selected_window = st.radio('When during the menstrual cycle is the fertile window? ', ['Everyday',
                                                                                          'Right Before the Start of a Period', 
                                                                                          'A Few Days Before Ovulation'])
   selected_days = st.radio('Approximately how many days in a cycle is a woman usually fertile? ', ['Two Days',
                                                                                                    'Six Days', 
                                                                                                    'Ten Days', 
                                                                                                    'Fourteen Days'])
   selected_order = st.radio('What is the order of the processes/phases of the menstrual cycle? ', ['Fertile Phase, Pre-menstrual, Period',
                                                                                                    'Ovulation, Fertile Phase, Pre-menstrual, Menstrual Phase', 
                                                                                                    'Lonianting Phase, Obseum Phase, Pre-menstrual, Menstrual Phase', 
                                                                                                    'Menstruation, Follicular Phase, Ovulation, Luteal Phase'])
   selected_hormone = st.radio('Which hormone is dominant only during ovulation? ', ['Progesterone',
                                                                                    'Luteinizing hormone', 
                                                                                    'Estrogen',
                                                                                    'Cortisol'])
   selected_loss = st.radio('How much blood is typically lost during a period? ', ['Two tablespoons',
                                                                                    'Quarter Cup', 
                                                                                    'Half a Cup',
                                                                                    'Whole Cup'])
   submitted = st.form_submit_button("Submit and Grade")

   if submitted:
       st.balloons()
       st.success('Your quiz has been submitted!')

quiz_df = pd.DataFrame(columns=['Sex', 'Cycle_Length', 'Fertile_Window_Timing', 'Fertile_Days', 'Cycle_Phases_Order', 
                                'Ovulation_Dominant_Hormone', 'Blood_Loss'])
quiz_df = {
    'Sex': [selected_sex],
    'Cycle_Length': [selected_length],
    'Fertile_Window_Timing': [selected_window],
    'Fertile_Days': [selected_days],
    'Cycle_Phases_Order': [selected_order],
    'Ovulation_Dominant_Hormone': [selected_hormone],
    'Blood_Loss': [selected_loss]
}

if submitted:
       st.write("Done")

# To-Do
#   Figure out how to reset the radio buttons when page is first opened
#   Grade the quiz and make total score
#   Display correct answers with success and error messages
#   Make it such that the df keeps growing and is saved
#   Make by sex histograms to compare results with all others who have taken this quiz