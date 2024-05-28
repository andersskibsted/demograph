def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    #df.info()




    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?

    #men_age_mean = df[df['sex'] == 'Male'].get('age').mean()
    average_age_men = df[df['sex'] == 'Male'].get('age').mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    number_of_bachelors = df['education'].value_counts().get('Bachelors', 0)
    
    percentage_bachelors = ((number_of_bachelors / df['education'].size) * 100).round(1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    edu_series = df['education']
    bachelors_bool = df['education'] == 'Bachelors'
    masters_bool = df['education'] == 'Masters'
    doctorate_bool = df['education'] == 'Doctorate'
    
    
    higher_edu_bool = bachelors_bool | masters_bool | doctorate_bool

    higher_education_50k = df[higher_edu_bool]['salary'] == '>50K'
    higher_education = higher_edu_bool.sum()

    lower_edu_bool = ~higher_edu_bool

    lower_education_50k = df[~higher_edu_bool]['salary'] == '>50K'
    
    lower_education = lower_edu_bool.sum()

    # percentage with salary >50K
    higher_education_rich = ((higher_education_50k.sum() / higher_education) * 100).round(1)
    lower_education_rich = ((lower_education_50k.sum() / lower_education) * 100).round(1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    works_min_hours = df[df['hours-per-week'] == min_work_hours]
    works_min_hours_rich = works_min_hours['salary'] == '>50K'
    num_min_workers = works_min_hours.size

    rich_percentage = ((works_min_hours_rich.sum() / num_min_workers) * 100).round(1)

    # What country has the highest percentage of people that earn >50K?
    total_in_countries = df['native-country'].value_counts()
    high_earners = df[df['salary'] == '>50K']
    high_earners_in_countries = high_earners['native-country'].value_counts()
    high_earners_in_countries_perc = high_earners_in_countries/total_in_countries
      
    highest_earning_country = high_earners_in_countries_perc.idxmax()
    highest_earning_country_percentage = (high_earners_in_countries_perc.max() * 100).round(1)

    # Identify the most popular occupation for those who earn >50K in India.
    high_earners_in = df['salary'] == '>50K'
    india = df['native-country'] == 'India'
    high_earners_in_India_bool = high_earners_in & india
    df[high_earners_in_India_bool]['occupation'].value_counts().idxmax()
    top_IN_occupation = df[high_earners_in_India_bool]['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)
    
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    
    }
    