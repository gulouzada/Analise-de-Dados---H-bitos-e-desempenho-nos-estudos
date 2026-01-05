import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/Users/gustavolouzada/Documents/habitos_na_performance_do_estudo/student_habits_performance.csv')

cols = [
    'study_hours_per_day',
    'social_media_hours',
    'netflix_hours',
    'attendance_percentage',
    'sleep_hours',
    'exercise_frequency',
    'mental_health_rating',
    'exam_score'
]

def correlacao_habitos_estudos():
    sns.heatmap(df[cols].corr(), annot=True, cmap='coolwarm')
    plt.title('Correlação entre hábitos e nota final')
    plt.show()

def horas_estudo_desempenho():
    sns.lmplot(data=df, x='study_hours_per_day', y='exam_score')
    plt.title('Relação entre horas de estudo e nota final')
    plt.show()

def diferenca_desempenho_horas_estudo():
    filtro_estudo_alto = df['study_hours_per_day'] > 5
    filtro_estudo_baixo = df['study_hours_per_day'] < 2

    grupo_estudo_alto = df[filtro_estudo_alto]['exam_score']
    grupo_estudo_baixo = df[filtro_estudo_baixo]['exam_score']

    return f"Média notas (estuda > 5h por dia): {grupo_estudo_alto.mean()}\nMédia notas (estuda < 2h por dia): {grupo_estudo_baixo.mean()}"

def redes_socias_e_desempenho():
    sns.histplot(data=df, x='social_media_hours')
    plt.title('Distribuição de tempo em redes sociais.')
    plt.show()

def intervalos_redes_socias_e_desempenho():
    df['social_media_bin'] = pd.cut(
        df['social_media_hours'],
        bins = [0, 2, 4, 6],
        labels = ['0-2h', '2-4h', '4-6h']           
    )
    sns.boxplot(data=df, x='social_media_bin', y='exam_score')
    plt.title('Notas por tempo em redes sociais.')
    plt.show()

def saude_e_desempenho():
    tradutor = {
        'diet_quality':'alimentação saudável',
        'exercise_frequency':'exercício físico',
        'mental_health_rating':'saúde mental'
    }
    for col in ['diet_quality', 'exercise_frequency', 'mental_health_rating']:
        sns.boxplot(data=df, x= col, y='exam_score')
        plt.title(f'Relação entre {tradutor[col]} e nota final.')
        plt.show()

print(correlacao_habitos_estudos())
print(horas_estudo_desempenho())
print(diferenca_desempenho_horas_estudo())
print(redes_socias_e_desempenho())
print(intervalos_redes_socias_e_desempenho())
print(saude_e_desempenho())
