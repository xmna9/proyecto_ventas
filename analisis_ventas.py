import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
df = pd.read_csv("ventas_productos.csv")

# Calcular el precio total por producto
df["Precio Total"] = df["Cantidad"] * df["Precio"]

# Crear el gráfico de barras
plt.figure(figsize=(8, 5))
plt.bar(df["Producto"], df["Precio Total"], color='skyblue')
plt.xlabel("Productos")
plt.ylabel("Precio Total")
plt.title("Precio Total por Producto")
plt.savefig("grafico_ventas.png")  # Guardar el gráfico como PNG
plt.show()
