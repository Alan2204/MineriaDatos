import pandas as pd
import statsmodels.api as sm


def anova(df):
    formula = "Global_Sales ~ Genre"
    modelo = sm.formula.ols(formula, data=df).fit()
    tabla= sm.stats.anova_lm(modelo, type=2)
    print(tabla)
    

df = pd.read_csv("csv/Video_Games.csv")
anova(df)