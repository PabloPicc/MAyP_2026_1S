
import matplotlib.pyplot as plt

# Datos de ejemplo
fechas = ['2015-01', '2015-02', '2015-03', '2015-04']
hectolitros = [120, 150, 110, 180]  # Eje Y principal (Izquierda)
precio_promedio = [45, 48, 52, 50]    # Eje Y secundario (Derecha)

# 1. Crear la figura y el primer eje (ax1)
fig, ax1 = plt.subplots()

# Graficar la primera serie (Hectolitros)
color_1 = 'tab:blue'
ax1.set_xlabel('Meses (2015)')
ax1.set_ylabel('Hectolitros de Vino', color=color_1)
ax1.plot(fechas, hectolitros, color=color_1, marker='o', label='Volumen')
ax1.tick_params(axis='y', labelcolor=color_1)

# 2. Crear el segundo eje que comparte el mismo eje X
ax2 = ax1.twinx() 

# Graficar la segunda serie (Precio)
color_2 = 'tab:red'
ax2.set_ylabel('Precio Promedio ($)', color=color_2)
ax2.plot(fechas, precio_promedio, color=color_2, linestyle='--', marker='s', label='Precio')
ax2.tick_params(axis='y', labelcolor=color_2)

# Ajustes finales
plt.title('Producción vs Precio de Vino')
fig.tight_layout() # Para que no se encimen las etiquetas
plt.show()



