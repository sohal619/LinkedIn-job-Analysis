import streamlit as st
from streamlit_option_menu import option_menu
from backend import Data
import pandas as pd

st.set_page_config(page_title='Job Analysis', page_icon=':star:')
data = Data()

selected = option_menu(
    menu_title=None,
    options=['Home', 'View Jobs'],
    icons=['house', 'book'],
    orientation='horizontal'
)
placeholder = st.empty()


if selected == 'Home':
    with open('jobs_data.csv', 'w') as file:
        file.write('.')
    with placeholder.container():
        st.image('https://img.icons8.com/color/512/linkedin.png', width=70)
        st.title(":blue[LinkedIn Job Analysis]")
        skill = st.text_input('Search skill (keyword/s)  👇')
        search_button = st.button('Search🔍')
        st.write('_____________________________________________________________________')
        st.write("""### A warm Welcome , Please write a skill.......""")

    if search_button:
        with open('jobs_data.csv', 'w') as file:
            file.write('.')
        if skill == '':
            st.write(":red[Enter Skill is required ⚠]")
        else:
            placeholder.empty()
            related_data = data.data_sender(skill.upper())
            st.write(f'### Most common Experience level: {related_data[1]}')
            st.write(f'### Most common Industry: {related_data[2]}')
            st.write(f'### Most common Company class: {related_data[3]}')
            st.write(f'### Total Number of Jobs Available: {related_data[4]}')
            if related_data[4] == 0:
                with open('jobs_data.csv', 'w') as file:
                    file.write('.')
            else:
                related_data[0].to_csv('jobs_data.csv', index=False)


jobs_data = pd.read_csv('jobs_data.csv')
if selected == 'View Jobs':
    if len(jobs_data) == 0:
        st.write('# Please, firstly search for skill/s. 🙂')
    else:
        st.dataframe(jobs_data)

st.write(f"Source Code: [GitHub](https://github.com/sohal619/LinkedIn-job-Analysis)")
st.write(f"Connect Me: [LinkedIn](https://www.linkedin.com/in/mohammad-sohal-5b8b38224/)")
