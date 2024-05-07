import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(layout="wide")

st.title('Menstrual Knowledge Quiz')

@st.cache_data
def load_data(csv):
    df=pd.read_csv(csv)
    return df
df = load_data('Survey_Responses_Cleaned - Sheet1.csv')

tab1, tab2 = st.tabs(["Quiz 📝", "Answers 📊"])

with tab1:
    with st.form("my_form"):
        st.info("Test Your Knowledge of Menstrual Cycles!")
        st.write("(The answers tab will become available only after this quiz is submitted.)")

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
                                                                                            'Luteinizing Hormone', 
                                                                                            'Estrogen',
                                                                                            'Cortisol'])
        selected_loss = st.radio('How much blood is typically lost during a period? ', ['Two tablespoons',
                                                                                            'Quarter Cup', 
                                                                                            'Half a Cup',
                                                                                            'Whole Cup'])
        submitted = st.form_submit_button("Submit and Grade")

        if submitted:
            st.balloons()

            score = 0
            if selected_length == "28 Days":
                    score += 1
            if selected_window == "A Few Days Before Ovulation":
                    score += 1
            if selected_days == "Six Days":
                    score += 1
            if selected_order == "Menstruation, Follicular Phase, Ovulation, Luteal Phase":
                    score += 1
            if selected_hormone == "Luteinizing Hormone":
                    score += 1
            if selected_loss == "Quarter Cup":
                    score += 1
            st.success("Your total score is: " + str(score) + "!") 
            st.toast("You may now look at the answers tab above to learn more! 😊")
if submitted:
    with tab2:
        st.success('''Below are the correct answers to the questions, sources for more information, and the distribution of responses from our sample.      
                   Hover over the bars to see more details and the complete response.''') 

        st.info("1. Approximately how long is a normal menstrual cycle?")
        st.write("Correct Answer: 28 days")
        st.write("Source: https://pubmed.ncbi.nlm.nih.gov/16700687/")
        alt_chart1 = alt.Chart(df).mark_bar().encode(x=str("Cycle_Length"), y='count()', color = "Sex").configure_axisX(labelAngle=45).interactive()
        st.altair_chart(alt_chart1, use_container_width=True)

        st.info("2. When during the menstrual cycle is the fertile window?")
        st.write("Correct Answer: A few days before ovulation.")
        st.write("Source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC27529/#:~:text=During%20the%20average%20woman%27s%20menstrual,the%20day%20of%20ovulation%20itself")
        alt_chart2 = alt.Chart(df).mark_bar().encode(x=str("Fertile_Window_Timing"), y='count()', color = "Sex").configure_axisX(labelAngle=45).interactive()
        st.altair_chart(alt_chart2, use_container_width=True)

        st.info("3. Approximately how many days in a cycle is a female usually fertile?")
        st.write("Correct Answer: Six days")
        st.write("Source: https://pubmed.ncbi.nlm.nih.gov/7477165/")
        alt_chart3 = alt.Chart(df).mark_bar().encode(x=str("Fertile_Days"), y='count()', color = "Sex").configure_axisX(labelAngle=45).interactive()
        st.altair_chart(alt_chart3, use_container_width=True)

        st.info("4. What is the order of the processes/phases of the menstrual cycle?")
        st.write("Correct Answer: Menstruation, Follicular phase, Ovulation, Luteal phase")
        st.write("Source: https://www.ncbi.nlm.nih.gov/books/NBK279054/")
        alt_chart4 = alt.Chart(df).mark_bar().encode(x=str("Cycle_Phases_Order"), y='count()', color = "Sex").configure_axisX(labelAngle=45).interactive()
        st.altair_chart(alt_chart4, use_container_width=True)

        st.info("5. Which hormone is dominant only during ovulation?")
        st.write("Correct Answer: Luteinizing Hormone (LH)")
        st.write("Source: https://www.ncbi.nlm.nih.gov/books/NBK441996/")
        alt_chart5 = alt.Chart(df).mark_bar().encode(x=str("Ovulation_Dominant_Hormone"), y='count()', color = "Sex").configure_axisX(labelAngle=45).interactive()
        st.altair_chart(alt_chart5, use_container_width=True)

        st.info("6. How much blood is typically lost during a period?")
        st.write("Correct Answer: Quarter cup")
        st.write("Source: https://www.ncbi.nlm.nih.gov/books/NBK279294/")
        alt_chart6 = alt.Chart(df).mark_bar().encode(x=str("Blood_Loss"), y='count()', color = "Sex").configure_axisX(labelAngle=45).interactive()
        st.altair_chart(alt_chart6, use_container_width=True)