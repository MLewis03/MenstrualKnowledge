import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(layout="wide")

st.title('Capstone Project: Descriptive Statistics')

df = pd.read_csv("Survey_Responses_Cleaned - Sheet1.csv")

answers  = {
    'cycle_length': "28 days",
    'fertile_window_timing': "A few days before ovulation",
    'fertile_days': "Six Days",
    'cycle_phases_order': "Menstruation, Follicular Phase, Ovulation, Luteal Phase",
    'ovulation_dominant_hormone': "Luteinizing hormone",
    'blood_loss': "Quarter cup"
}

for column, correct_answer in answers.items():
    df[f'{column}_score'] = df[column].apply(lambda x: 1 if str(x).strip().lower() == correct_answer.lower() else 0)

df['total_knowledge_score'] = df.filter(like='_score').sum(axis=1)

menstrual_education_importance_encoding = {"Not at all": 1, "Of little importance": 2, "Important": 3, "Essential" : 4}
df['menstrual_education_importance'] = df['menstrual_education_importance'].replace(menstrual_education_importance_encoding)

menstrual_education_in_school_encoding = {"Strongly disagree": 1, "Disagree": 2, "Agree": 3, "Strongly agree": 4}
df['menstrual_education_in_school'] = df['menstrual_education_in_school'].replace(menstrual_education_in_school_encoding)

impact_on_functioning_encoding = {"Not noticeable, no impact on functioning.": 1, "Mild inconvenience, doesn't greatly affect functioning.": 2, "Somewhat difficult, but manageable.": 3, "Very burdensome, significantly impairs functioning.": 4}
df['impact_on_functioning'] = df['impact_on_functioning'].replace(impact_on_functioning_encoding)
df['total_attitude_score'] = df['comfort_level'] + df['menstrual_education_importance'] + df['menstrual_education_in_school'] + df['impact_on_functioning']

df = df[df['uncc_affiliation'] != 'Alumni']

st.sidebar.header('Input')
selected_x_var = st.sidebar.selectbox('What do you want the variable to be?', df.columns)
selected_gender = st.sidebar.selectbox('What gender do you want to filter for?',['all', 'male', 'female'])
#selected_color = st.sidebar.selectbox('What would you like to color by?"', df.columns)

if selected_gender == 'male':
    df = df[df['sex'] == 'Male']
elif selected_gender == 'female':
    df = df[df['sex'] == 'Female']
else:
    pass

alt_chart = ((alt.Chart(df, title=f"Histogram of Responses")).mark_bar().encode(x=selected_x_var, y='count()', color='sex').interactive())
st.altair_chart(alt_chart, use_container_width=True)

#alt_chart2 = alt.Chart(df).transform_joinaggregate(
#    Total=df.count(),
#).transform_calculate(
#    PercentOfTotal= (selected_x_var / 'Total')
#).mark_bar().encode(
#    alt.X('PercentOfTotal:Q', axis=alt.Axis(format='.0%')),
#    Y=selected_x_var
#)
#st.altair_chart(alt_chart2, use_container_width=True)