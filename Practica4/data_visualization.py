import pandas as pd
import matplotlib.pyplot as plt

def ventas_europa(df):
    prueba = df.groupby(["Year_of_Release"])[["EU_Sales"]].sum()
    plt.plot(prueba)
    plt.ylabel("Ventas Europa")
    plt.xlabel("Años")
    plt.show()


def graficar(df):
    prueba = df.groupby(["Year_of_Release"])[["Global_Sales"]].sum()
    plt.plot(prueba)
    plt.ylabel("Ventas Globales")
    plt.xlabel("Años")
    plt.show()
    

df = pd.read_csv("csv/Video_Games.csv")
graficar(df)
ventas_europa(df)
