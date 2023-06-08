import matplotlib.pyplot as plt

def graficarPromedio(dataFrame,columnaEjeX,columnaInteres,nombreGrafica):
    
     colores = ['blue', 'green', 'red', 'orange']
     
     arboles_promedio = dataFrame.groupby(columnaEjeX)[columnaInteres].mean()
     plt.bar(arboles_promedio.index, arboles_promedio,color=colores)
     plt.xlabel('Ciudad')
     plt.ylabel('Vereda')
     plt.title('Promedio de Arboles sembrados')
     plt.savefig(f'./assets/img/{nombreGrafica}.png', dpi=300, bbox_inches='tight')