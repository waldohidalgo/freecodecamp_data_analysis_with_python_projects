# Data Analysis with Python Projects

Repositorio con el código solución a los 5 proyectos requisitos obligatorios para obtener la [Data Analysis with Python Certification](https://www.freecodecamp.org/learn/data-analysis-with-python/)

Hasta la fecha llevo realizado: Proyecto 1, 2 y 3. A medida que vaya realizando el resto de proyectos los iré subiendo a este repositorio.

## Listado de Proyectos

### 1- Mean-Variance-Standard Deviation Calculator

#### 1.1- Proyecto Aprobado

![Primer Proyecto Aprobado](./Proyecto1_Mean-Variance-StandardDeviationCalculator/passed.webp)

#### 1.2- Todos los tests superados

![All tests passed](./Proyecto1_Mean-Variance-StandardDeviationCalculator/all_tests_passed.webp)

#### 1.3- Código Creado

```py
import numpy as np

def calculate(list):
    n=len(list)
    if n<9:
        raise ValueError("List must contain nine numbers.")

    orig=np.array(list)
    reorg=orig.reshape(3,3)
    mean=[np.mean(reorg,axis=0).tolist(),np.mean(reorg,axis=1).tolist(),np.mean(reorg)]
    variance=[np.var(reorg,axis=0).tolist(),np.var(reorg,axis=1).tolist(),np.var(reorg)]
    std=[np.std(reorg,axis=0).tolist(),np.std(reorg,axis=1).tolist(),np.std(reorg)]
    maxv=[np.max(reorg,axis=0).tolist(),np.max(reorg,axis=1).tolist(),np.max(reorg)]
    minv=[np.min(reorg,axis=0).tolist(),np.min(reorg,axis=1).tolist(),np.min(reorg)]
    sumv=[np.sum(reorg,axis=0).tolist(),np.sum(reorg,axis=1).tolist(),np.sum(reorg)]

    calculations={
        'mean':mean,
        'variance':variance,
        'standard deviation':std,
        'max':maxv,
        'min':minv,
        'sum':sumv
    }

    return calculations
```

### 2- Demographic Data Analyzer

El archivo CSV utilizado llamado **adult.data.csv** NO lo he cargado en mi repositorio por pesar demasiado. Sin embargo, el archivo se encuentra en la siguiente URL: [Link a Archivo](https://github.com/freeCodeCamp/boilerplate-demographic-data-analyzer/blob/main/adult.data.csv)

#### 2.1- Proyecto Aprobado

![Segundo Proyecto Aprobado](./Proyect2_DemographicDataAnalyzer/passed.webp)

#### 2.2- Todos los tests superados

![All tests passed](./Proyect2_DemographicDataAnalyzer/all_test_passed.webp)

#### 2.3- Código Creado

El código que he creado va después de los comentarios. Cada comentario se refiere a lo que se pide realizar.

```py
def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df.sex=='Male'].age.mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(((df.education[df.education=="Bachelors"].count())/(df.education.count()))*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df.education.isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df.education.isin(['Bachelors', 'Masters', 'Doctorate'])]

    # percentage with salary >50K
    higher_education_rich = round((higher_education.salary[higher_education.salary=='>50K'].count()/higher_education.salary.count())*100,1)
    lower_education_rich = round((lower_education.salary[lower_education.salary=='>50K'].count()/lower_education.salary.count())*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = round(df['hours-per-week'].min(),1)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = round((df.loc[df['hours-per-week']==df['hours-per-week'].min(),['salary']].value_counts())['>50K'],1)

    rich_percentage = round((df.loc[df['hours-per-week']==df['hours-per-week'].min(),['salary']].value_counts(normalize=True)*100)['>50K'],1)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = df.groupby(['native-country', 'salary']).size().unstack(fill_value=0).apply(lambda x: (x / x.sum()) * 100, axis=1)['>50K'].idxmax()
    #otra forma pd.crosstab()
    highest_earning_country_percentage =round(df.groupby(['native-country', 'salary']).size().unstack(fill_value=0).apply(lambda x: (x / x.sum()) * 100, axis=1)['>50K'].max(),1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.loc[(df.salary=='>50K')& (df['native-country']=='India'),['occupation']].mode().iloc[0,0]

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
```

### 3- Medical Data Visualizer

El archivo CSV utilizado llamado **medical_examination.csv** NO lo he cargado en mi repositorio por pesar demasiado. Sin embargo, el archivo se encuentra en la siguiente URL: [Link a Archivo](https://github.com/freeCodeCamp/boilerplate-medical-data-visualizer/blob/main/medical_examination.csv)

#### 3.1- Proyecto Aprobado

![Tercer Proyecto Aprobado](./Proyecto3_MedicalDataVisualize/passed.webp)

#### 3.2- Todos los tests superados

![All tests passed](./Proyecto3_MedicalDataVisualize/all_tests_passed.webp)

#### 3.3- Código Creado

La generación de cortes cambia el tipo de datos a categorico lo que provoca errores en los tests si no se modifica. Para evitar el cambio de tipo de datos he utilizado el método **where**.

```py
# 1
df = pd.read_csv("medical_examination.csv")

# 2
# df['overweight'] = pd.cut(df['weight']/(df['height']/100)**2,bins=[0,25,np.inf],labels=[0,1])
df['overweight']=np.where(df['weight']/(df['height']/100)**2<=25,0,1)

# 3
#df['gluc']=pd.cut(df['gluc'],bins=[0,1,np.inf],labels=[0,1])
#df['cholesterol']=pd.cut(df['cholesterol'],bins=[0,1,np.inf],labels=[0,1])

df['gluc']=np.where(df['gluc'] <= 1, 0, 1)
df['cholesterol']=np.where(df['cholesterol']<=1,0,1)

# 4
def draw_cat_plot():
    # 5
    variables=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
    df_cat = pd.melt(df,id_vars=['cardio'],value_vars=variables)


    # 6
    df_cat = df_cat.groupby(["cardio", "variable", "value"]).size().reset_index().rename(columns={0:'total'})

    # 7

    # 8
    fig = sns.catplot(data=df_cat, x="variable", y="total", hue="value", col="cardio",  kind="bar", height=4, aspect=1.5 ).figure


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    f1=(df['ap_lo'] <= df['ap_hi'])
    f2=(df['height'] >= df['height'].quantile(0.025))
    f3=(df['height'] <= df['height'].quantile(0.975))
    f4=(df['weight'] >= df['weight'].quantile(0.025))
    f5=(df['weight'] <= df['weight'].quantile(0.975))

    # 11
    df_heat = df[f1 & f2 & f3 & f4 &f5]

    # 12
    corr = df_heat.corr()

    # 13
    mask=np.triu(np.ones(corr.shape), 0).astype(bool)

    # 14
    fig, ax =plt.subplots(figsize=(12, 6))

    # 15

    sns.heatmap(corr, mask=mask, annot=True, linewidths=0.5, ax=ax,cmap='inferno',fmt=".1f")

    # 16
    fig.savefig('heatmap.png')
    return fig
```

#### 3.3- Gráficos Generados

##### 3.3.1- Gráfico de Columnas

![Gráfico de Columnas](./Proyecto3_MedicalDataVisualize/catplot.png)

##### 3.3.2- Mapa de Calor

![Mapa de Calor](./Proyecto3_MedicalDataVisualize/heatmap.png)
