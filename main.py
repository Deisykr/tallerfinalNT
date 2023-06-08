import pandas as pd
from helpers.creartablasHTML import crearTabla
from helpers.creargrafica import graficarPromedio

from dpdf import FPDF


tabla1=pd.read_csv("./data/Siembras.csv")
print(tabla1.head())

#Ticket,Nombre comun,Fecha,evento,Ciudad,Vereda,Arboles,Hectareas
#FILTRANDO O APLICANDO CONDICIONES
# FILTRO1:
santaFe=tabla1.query('Arboles>250 and Ciudad=="Santa Fe de Antioquia"')
#print(santaFe)
#print('\n')
#FILTRO2:
caucasia1=tabla1.query('Ciudad=="Caucasia"')
#print('\n')
print(caucasia1)
print(caucasia1.describe())
#FILTRO 3: 
belmira1=tabla1.query('Ciudad=="Belmira" & Vereda=="La Salazar"')
belmira2=tabla1.query('Ciudad=="Belmira" & Vereda=="Rio Arriba"')
#print(belmira1)
#print('\n') 
#FILTRO 4: 
bello1=tabla1.query('Ciudad=="Bello" & Vereda=="Quitasol"')
#print('\n') 
#print(bello1)
#print(bello1.describe())
#FILTRO 5: 
caramanta1=tabla1.query('Arboles>100 and Ciudad=="Caramanta"')
#print(caramanta1)
#print('\n')
#FILTRO 6: 
yarumal1=tabla1.query('Ciudad=="Yarumal" & Vereda=="Mallarino"')
#print('\n') 
#print(yarumal1)

#Generemos las tablas para el reporte
crearTabla(santaFe,"Santafe")
crearTabla(caucasia1,"Caucasia")
crearTabla(belmira1,"LaSalazar")
crearTabla(belmira2,"RioArriba")
crearTabla(bello1,"Quitasol")
crearTabla(caramanta1,"Caramanta")
crearTabla(yarumal1,"Mallarino")




#Generamos graficas
graficarPromedio(santaFe,'Ciudad','Vereda','Arboles','grafiarbol')
graficarPromedio(caucasia1,'Ciudad','Vereda','Arboles','grafiarbol')
graficarPromedio(belmira1,'Ciudad','Vereda','Arboles','grafiarbol')
graficarPromedio(belmira2,'Ciudad','Vereda','Arboles', 'grafiarbol')
graficarPromedio(bello1,'Ciudad','Vereda','Arboles', 'grafiarbol')
graficarPromedio(yarumal1,'Ciudad','Vereda','Arboles', 'grafiarbol')



#graficarTortaSalarios(analistas1,[20,30,40,50,60],'edad','salario','promediosAnalistas1')
#graficarTortaSalarios(analistas2,[20,30,40,50,60],'edad','salario','promediosAnalistas1')




