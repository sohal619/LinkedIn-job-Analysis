import streamlit as st
from streamlit_option_menu import option_menu
import pickle


class Data:
    def __init__(self):
        with open('final_data.pkl', 'rb') as file:
            self.df = pickle.load(file)

        self.skills = ['PYTHON', 'C++', 'JAVA', 'HADOOP', 'SCALA', 'FLASK',
                       'PANDAS', 'SPARK', 'NUMPY', 'PHP', 'SQL', 'MYSQL', 'CSS', 'MONGODB',
                       'NLTK', 'TENSORFLOW', 'LINUX', 'RUBY', 'JAVASCRIPT', 'DJANGO', 'REACT',
                       'REACTJS', 'AI', 'UI', 'TABLEAU', 'NODEJS', 'EXCEL', 'POWER BI',
                       'SELENIUM', 'HTML', 'ML']

        self.experience_level = 'Not available'
        self.industry = 'Not available'
        self.company_class = 'Not available'
        self.num_of_jobs = 0

    def data_sender(self, skill):
        for i in self.skills:
            if i in skill:
                self.df = self.df[self.df[i] == 1]
                self.experience_level = self.df['Involvement'].mode()[0].strip(' ')
                self.industry = self.df['Industry'].mode()[0].strip(' ')
                self.company_class = self.df['Class'].mode()[0].strip(' ')
                self.num_of_jobs = len(self.df)
        self.df = self.df[['Name', 'Class', 'Designation', 'Location', 'Total_applicants',
                           'LinkedIn_Followers', 'Level', 'Involvement', 'Employee_count',
                           'Industry']]
        return self.df, self.experience_level, self.industry, self.company_class, self.num_of_jobs


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
            related_data = data.data_sender(skill.upper())
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
