import pandas as pd

#Data frame contiene la informacion basica con el nombre de las piezas
#Y los centimetros para poder armar el excel

data={
    "Piezas": ["Pata","Tablero","Puerta","Estante","Panel Lateral"],
    "centimetros":[40,120,50,35,190]
}

df=pd.DataFrame(data)

df.to_excel("muebles_medidas.xlsx",index=False)
