import pandas as pd 
df = pd.read_csv('adult.data.csv')

# Get the dataframe informations 
df.info()

# first 5 rows of the dataframe
df.head()

# How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.

race_count = df['race'].value_counts()

# What is the average age of men?
average_age_men = df.loc[df['sex'] == 'Male','age'].mean()


# What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = (df['education'].value_counts()['Bachelors']/len(df))*100


# What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
# What percentage of people without advanced education make more than 50K? 
# with and without `Bachelors`, `Masters`, or `Doctorate`
 
higher_education = df[((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'))].value_counts().sum()
lower_education = df[~((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'))].value_counts().sum()


# percentage with salary >50K

higher_education_rich = ((df[((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')) & (df['salary'] == '>50K')].value_counts().sum() / higher_education) * 100).round(1)
lower_education_rich = ((df[~((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')) & (df['salary'] == '>50K')].value_counts().sum() / lower_education) * 100).round(1)


# What is the minimum number of hours a person works per week (hours-per-week feature)?

min_work_hours = df['hours-per-week'].min()


# What percentage of the people who work the minimum number of hours per week have a salary of >50K?

num_min_workers = df[(df['salary'] == '>50K') & (df['hours-per-week'] == min_work_hours)].value_counts().sum()
rich_percentage = (num_min_workers / df[df['hours-per-week'] == df['hours-per-week'].min()].value_counts().sum()) * 100 


# What country has the highest percentage of people that earn >50K?
highest_earning_country = ((df[df['salary'] == '>50K']['native-country'].value_counts()) / (df['native-country'].value_counts()) * 100).sort_values(ascending=False).idxmax()

# highest_earning_country_percentage = None
highest_earning_country_percentage = ((df[(df['native-country'] == highest_earning_country) & (df['salary'] == '>50K')].value_counts().sum() / (df[(df['native-country'] == highest_earning_country)]).value_counts().sum()) * 100).round(1)


# Identify the most popular occupation for those who earn >50K in India.

top_IN_occupation = df[(df['salary'] == '>50K') & (df['native-country'].isin(['India']))].groupby('occupation')['occupation'].count().idxmax()






