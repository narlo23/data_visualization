import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(16,6))
life_expectancy=pd.read_csv('./csv/Life Expectancy Data.csv')
health_expenditure=pd.read_csv('./csv/Expenditure_on_Health.csv')

plt.subplot(121)
disease=life_expectancy[["Life expectancy ", "Hepatitis B", "Measles ", "Polio", " HIV/AIDS", " thinness  1-19 years"]]
sns.heatmap(data=disease.corr(), annot=True, annot_kws={"size":7}, cmap="OrRd")
plt.title("disease & life expectancy", fontsize=20)
plt.yticks(rotation=0)
plt.xticks(rotation=45)

plt.subplot(122)
social=life_expectancy[["Life expectancy ", "Status", "Alcohol", "GDP", "Population", "Schooling"]]
sns.heatmap(data=social.corr(), annot=True, annot_kws={"size":7}, cmap="GnBu")
plt.title("social, economy & life expectancy", fontsize=20)
plt.yticks(rotation=0)
plt.xticks(rotation=45)

plt.show()              #1-2

fig=plt.figure(figsize=(16,6))
plt.subplot(121)
first_country=life_expectancy[life_expectancy["Country"]=='Japan']
second_country=life_expectancy[life_expectancy["Country"]=='Iceland']
third_country=life_expectancy[life_expectancy["Country"]=='Switzerland']
fourth_country=life_expectancy[life_expectancy["Country"]=='Sweden']
sns.lineplot(x="Year", y="Life expectancy ", data=first_country, color='royalblue', label='Japan')
sns.lineplot(x="Year", y="Life expectancy ", data=second_country, color='coral', label='Iceland')
sns.lineplot(x="Year", y="Life expectancy ", data=third_country, color='mediumspringgreen', label='Switzerland')
sns.lineplot(x="Year", y="Life expectancy ", data=fourth_country, color='mediumvioletred', label='Sweden')
plt.title("Life expectancy changes in the top 4 countries(As of 2000)")

plt.subplot(122)
country_1st=life_expectancy[life_expectancy["Country"]=='Malawi']
country_2nd=life_expectancy[life_expectancy["Country"]=='Zambia']
country_3rd=life_expectancy[life_expectancy["Country"]=='Angola']
country_4th=life_expectancy[life_expectancy["Country"]=='Uganda']
sns.lineplot(x="Year", y="Life expectancy ", data=country_1st, color='deepskyblue', label='Malawi')
sns.lineplot(x="Year", y="Life expectancy ", data=country_2nd, color='pink', label='Zambia')
sns.lineplot(x="Year", y="Life expectancy ", data=country_3rd, color='gold', label='Angola')
sns.lineplot(x="Year", y="Life expectancy ", data=country_4th, color='mediumslateblue', label='Uganda')
plt.title("Life expectancy changes in the lower 4 countries(As of 2000)")

plt.show()          #4-2


current_life_expectancy=life_expectancy[["Country", "Year", "Life expectancy "]]
health_expenditure=health_expenditure[["Country", "Year", "Series", "Value"]]
current_health_expenditure=health_expenditure[health_expenditure["Series"]=='Current health expenditure (% of GDP)']
domestic_health_expenditure=health_expenditure[health_expenditure["Series"]=='Domestic general government health expenditure (% of total government expenditure)']
all_data_1=pd.merge(left=current_life_expectancy, right=current_health_expenditure, on=['Country', 'Year'])
all_data_2=pd.merge(left=current_life_expectancy, right=domestic_health_expenditure, on=['Country', 'Year'])

fig = plt.figure(figsize=(10,6))
sns.regplot(x="Life expectancy ", y="Value", data=all_data_1, label='Current health expenditure (% of GDP)')
sns.regplot(x="Life expectancy ", y="Value", data=all_data_2, label='Domestic general government health expenditure (% of total government expenditure)')
plt.title("Life expectancy and health")
fig.legend(labels=['CHE(% of GDP)', 'GGHE(% of total government expenditure)'])
plt.show()          #3-1
