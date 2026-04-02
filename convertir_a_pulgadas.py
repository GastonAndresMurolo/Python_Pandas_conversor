import pandas as pd

def cm_a_pulgadas(cm):
    return cm / 2.56

df=pd.read_excel("muebles_medidas.xlsx")

df["Pulgadas"]=df["centimetros"].apply(cm_a_pulgadas)

df.to_excel("muebles_medidas_convertidas.xlsx",index=False)

