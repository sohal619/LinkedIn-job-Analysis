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
