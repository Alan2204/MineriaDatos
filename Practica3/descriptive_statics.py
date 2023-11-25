import pandas as pd

def ventas_anuales(df):
    year = df["Year_of_Release"].unique()
    year.sort()
    print(year)
    ventas = list()




def sumas(df):
    eu =sum(df["EU_Sales"])
    jp =sum(df["JP_Sales"])
    na =sum(df["NA_Sales"])
    other =sum(df["Other_Sales"])
    glob =sum(df["Global_Sales"])
    print("\n VENTAS TOTALES \n")
    print("Norte America:{:.2f}  Japon:{:.2f}  Europa:{:.2f}  Otros:{:.2f} Global:{:.2f}".format(na, jp, eu, other, glob))

df = pd.read_csv("csv/Video_Games.csv")
print(df.describe().round(2))
print()
print(df.describe(include=[object]).round(2)) #resumen estadistico
sumas(df)
ventas_anuales(df)

