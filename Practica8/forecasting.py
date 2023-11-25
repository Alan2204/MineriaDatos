import matplotlib.pyplot as plt
import statsmodels.api as sm
import numbers
import pandas as pd
from tabulate import tabulate


def print_tabulate(df):
    print(tabulate(df, headers=df.columns, tablefmt="orgtbl"))

def transform_variable(df, x):
    if isinstance(df[x][0], numbers.Number):
        return df[x] # type: pd.Series
    else:
        return pd.Series([i for i in range(0, len(df[x]))])

def linear_regression(df, x, y):
    fixed_x = transform_variable(df, x)
    model= sm.OLS(df[y],sm.add_constant(fixed_x)).fit()
    bands = pd.read_html(model.summary().tables[1].as_html(),header=0,index_col=0)[0]
    print_tabulate(pd.read_html(model.summary().tables[1].as_html(),header=0,index_col=0)[0])
    coef = pd.read_html(model.summary().tables[1].as_html(),header=0,index_col=0)[0]['coef']
    r_2_t = pd.read_html(model.summary().tables[0].as_html(),header=None,index_col=None)[0]
    return {'m': coef.values[1], 'b': coef.values[0], 'r2': r_2_t.values[0][3], 'r2_adj': r_2_t.values[1][3], 'low_band': bands['[0.025'][0], 'hi_band': bands['0.975]'][0]}

def plt_lr(df, x, y, m, b, r2, r2_adj, low_band, hi_band, colors):
    fixed_x = transform_variable(df, x)
    df.plot(x=x,y=y, kind='scatter')
    plt.plot(df[x],[ m * x + b for _, x in fixed_x.items()], color=colors[0])
    plt.fill_between(df[x],
                     [ m * x  + low_band for _, x in fixed_x.items()],
                     [ m * x + hi_band for _, x in fixed_x.items()], alpha=0.2, color=colors[1])





df = pd.read_csv("csv/Video_Games.csv") # type: pd.DataFrame
ventas = df.groupby(["Year_of_Release"])[["Global_Sales"]].sum().reset_index()
a = linear_regression(ventas, "Year_of_Release", "Global_Sales")
plt_lr(df=ventas, x="Year_of_Release", y="Global_Sales", colors=('red', 'orange'), **a)

plt.xticks(rotation=90)
plt.savefig('Practica8/ventas_anuales.png')
plt.close()