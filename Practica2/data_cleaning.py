import pandas as pd
from tabulate import tabulate

def print_tabulate(df):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

#Funcion para eliminar las filas con valores nulos

def limpieza_valoresnulos(df):
    df.dropna(how = 'any', inplace=True)
    
#Funcion para convertir los tipos de datos

def tipo_datos(datos):
   datos["Name"]=datos["Name"].astype(str)
   datos["Platform"]=datos["Platform"].astype(str)
   datos["Year_of_Release"]=datos["Year_of_Release"].astype(int)
   datos["Genre"]=datos["Genre"].astype("category")
   datos["Publisher"]=datos["Publisher"].astype(str)
   datos["NA_Sales"]=datos["NA_Sales"].astype(float)
   datos["EU_Sales"]=datos["EU_Sales"].astype(float)
   datos["JP_Sales"]=datos["JP_Sales"].astype(float)
   datos["Other_Sales"]=datos["Other_Sales"].astype(float)
   datos["Global_Sales"]=datos["Global_Sales"].astype(float)
   datos["Critic_Score"]=datos["Critic_Score"].astype(float)
   datos["Critic_Count"]=datos["Critic_Count"].astype(int)
   datos["User_Score"]=datos["User_Score"].astype(float)
   datos["User_Count"]=datos["User_Count"].astype(int)
   datos["Developer"]=datos["Developer"].astype(str)
   datos["Rating"]=datos["Rating"].astype("category")
      
df = pd.read_csv('Video_Games.csv/')
limpieza_valoresnulos(df)
tipo_datos(df)
print(df.dtypes)
l = "-"
print(l*32)
print_tabulate(df.head())
df.to_csv("csv\Video_Games.csv",index=False) #Guarda los cambios

