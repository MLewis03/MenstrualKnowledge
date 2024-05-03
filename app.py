import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(layout="wide")

st.title('Menstrual Knowledge Quiz')

df = pd.read_csv("Survey_Responses_Cleaned - Sheet1.csv")

df = df[df['UNCC_Affiliation'] != 'Alumni']

df = df['Sex', "Cycle_Length", "Fertile_Window_Timing", "Fertile_Days", "Cycle_Phases_Order", "Ovulation_Dominant_Hormone", "Blood_Loss"]

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

st.table(df)

# Make side by side sex chart
# Get rid of underscores in variable names
# Reset sex select box whenever variable selected changes
# Use st.form to make the quiz submittable
# Maybe include optional filter for sex or year in school using group.by in select boxes