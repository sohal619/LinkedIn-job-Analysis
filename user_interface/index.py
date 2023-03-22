import streamlit as st
from streamlit_option_menu import option_menu
import pickle

with open('final_data.pkl', 'rb') as file:
    df = pickle.load(file)

skills = ['PYTHON', 'C++', 'JAVA', 'HADOOP', 'SCALA', 'FLASK',
          'PANDAS', 'SPARK', 'NUMPY', 'PHP', 'SQL', 'MYSQL', 'CSS', 'MONGODB',
          'NLTK', 'TENSORFLOW', 'LINUX', 'RUBY', 'JAVASCRIPT', 'DJANGO', 'REACT',
          'REACTJS', 'AI', 'UI', 'TABLEAU', 'NODEJS', 'EXCEL', 'POWER BI',
          'SELENIUM', 'HTML', 'ML']

experience_level = 'Not available'
industry = 'Not available'
company_class = 'Not available'
num_of_jobs = 0


def data_sender(skill_key):
    global df, experience_level, industry, company_class, num_of_jobs
    for i in skills:
        if i in skill_key:
            df = df[df[i] == 1]
            experience_level = df['Involvement'].mode()[0].strip(' ')
            industry = df['Industry'].mode()[0].strip(' ')
            company_class = df['Class'].mode()[0].strip(' ')
            num_of_jobs = len(df)
    df = df[['Name', 'Class', 'Designation', 'Location', 'Total_applicants',
             'LinkedIn_Followers', 'Level', 'Involvement', 'Employee_count',
             'Industry']]
    return df, experience_level, industry, company_class, num_of_jobs


st.set_page_config(page_title='Job Analysis', page_icon=':star:')

selected = option_menu(
    menu_title=None,
    options=['Home', 'View Jobs'],
    icons=['house', 'book'],
    orientation='horizontal'
)
placeholder = st.empty()

if selected == 'Home':
    with open('jobs_data.pkl', 'wb') as file:
        pickle.dump('', file)
    with placeholder.container():
        st.image('https://img.icons8.com/color/512/linkedin.png', width=70)
        st.title(":blue[LinkedIn Job Analysis]")
        skill = st.text_input('Search skill (keyword/s)  👇')
        search_button = st.button('Search🔍')
        st.write('_____________________________________________________________________')
        st.write("""### A warm Welcome , Please write a skill.......""")

    if search_button:
        with open('jobs_data.pkl', 'wb') as file:
            pickle.dump('', file)
        if skill == '':
            st.write(":red[Enter Skill is required ⚠]")
        else:
            placeholder.empty()
            related_data = data_sender(skill.upper())
            st.write(f'### Most common Experience level: {related_data[1]}')
            st.write(f'### Most common Industry: {related_data[2]}')
            st.write(f'### Most common Company class: {related_data[3]}')
            st.write(f'### Total Number of Jobs Available: {related_data[4]}')
            if related_data[4] == 0:
                with open('jobs_data.pkl', 'wb') as file:
                    pickle.dump('', file)
            else:
                with open('jobs_data.pkl', 'wb') as file:
                    pickle.dump(related_data[0], file)

with open('jobs_data.pkl', 'rb') as file:
    jobs_data = pickle.load(file)

if selected == 'View Jobs':
    try:
        if jobs_data == '':
            st.write('# Please, firstly search for skill/s. 🙂')
    except ValueError:
        st.dataframe(jobs_data.reset_index(drop=True))

st.write(f"Source Code: [GitHub](https://github.com/sohal619/LinkedIn-job-Analysis)")
st.write(f"Connect Me: [LinkedIn](https://www.linkedin.com/in/mohammad-sohal-5b8b38224/)")
