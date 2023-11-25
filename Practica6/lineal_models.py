import pandas as pd
import statsmodels.api as sm
import numbers
from matplotlib import pyplot as plt

def transform_variable(df, x):
    if isinstance(df[x][0], numbers.Number):
        return df[x] # type: pd.Series
    else:
        return pd.Series([i for i in range(0, len(df[x]))])

def regresion_lineal(df):
    fixed_x = transform_variable(df, "Critic_Score")
    modelo_lineal = sm.OLS(df["Global_Sales"], sm.add_constant(fixed_x)).fit()
    print(modelo_lineal.summary())

    sales_perdiction = modelo_lineal.predict(pd.DataFrame(sm.add_constant(fixed_x)))
    print(sales_perdiction)
    plt.scatter(df["Critic_Score"], df["Global_Sales"])
    plt.plot(pd.DataFrame(sm.add_constant(fixed_x)), sales_perdiction, c="red", linewidth=3)
    plt.savefig(f'Practica6/lr_GlobalSales_CriticScore.png')
    plt.show()
    plt.close()

    

    
df = pd.read_csv("csv/Video_Games.csv")
regresion_lineal(df)


