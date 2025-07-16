import pandas as pd

def calculate_demographic_data(print_data=True):
    # Load data
    df = pd.read_csv('adult.data.csv')

    #Race count (using value_counts())
    race_count = df['race'].value_counts()

    #Average age of men (using query() for cleaner filtering)
    average_age_men = round(df.query('sex == "Male"')['age'].mean(), 1)

    #Percentage with Bachelors (using mean() * 100 for efficiency)
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    #Higher vs lower education rich percentages (using groupby)
    education_split = df.groupby(df['education'].isin(['Bachelors', 'Masters', 'Doctorate']))
    higher_education_rich = round(education_split['salary'].apply(lambda x: (x == '>50K').mean() * 100).loc[True], 1)
    lower_education_rich = round(education_split['salary'].apply(lambda x: (x == '>50K').mean() * 100).loc[False], 1)

    #Minimum work hours (using min())
    min_work_hours = df['hours_per_week'].min()

    #Rich percentage among minimal workers (using query)
    rich_percentage = round(
        df.query('hours_per_week == @min_work_hours')['salary'].eq('>50K').mean() * 100,
        1
    )

    #Country with highest % of rich (using groupby + transform)
    country_stats = (
        df.groupby('native-country')['salary']
        .apply(lambda x: (x == '>50K').mean() * 100)
        .round(1)
    )
    highest_earning_country = country_stats.idxmax()
    highest_earning_country_percentage = country_stats.max()

    #Top occupation in India for rich (using mode())
    top_IN_occupation = (
        df.query('`native-country` == "India" and salary == ">50K"')['occupation']
        .mode()[0]
    )

    #Print results if needed
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print(f"Country with highest percentage of rich: {highest_earning_country}")
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
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

#Run the function
calculate_demographic_data()