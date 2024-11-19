import tkinter as tk
import mysql.connector
from tkinter import messagebox
import matplotlib.pyplot as plt
import pandas as pd

# Función para conectar la base de datos
def conectar_db():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="campusfp",
            database="ENCUESTAS"
        )
        return conexion
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se puede conectar a la base de datos: {err}")
        return None

# Función para crear una encuesta
def crear_encuesta():
    conexion = conectar_db()
    if conexion:
        cursor = conexion.cursor()
        edad = entry_edad.get()
        sexo = entry_sexo.get()
        bebidas_semana = entry_bebidas_semana.get()
        cervezas_semana = entry_cervezas_semana.get()
        bebidas_fin_semana = entry_bebidas_fin_semana.get()
        bebidas_destiladas_semana = entry_bebidas_destiladas_semana.get()
        vinos_semana = entry_vinos_semana.get()
        perdidas_control = entry_perdidas_control.get()
        diversion_dependencia_alcohol = entry_diversion_dependencia_alcohol.get()
        problemas_digestivos = entry_problemas_digestivos.get()
        tension_alta = entry_tension_alta.get()
        dolor_cabeza = entry_dolor_cabeza.get()
        try:
            cursor.execute("""
                INSERT INTO ENCUESTA (edad, Sexo, BebidasSemana, CervezasSemana, BebidasFinSemana, 
                BebidasDestiladasSemana, VinosSemana, PerdidasControl, DiversionDependenciaAlcohol, 
                ProblemasDigestivos, TensionAlta, DolorCabeza) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana, bebidas_destiladas_semana, vinos_semana, perdidas_control, diversion_dependencia_alcohol, problemas_digestivos, tension_alta, dolor_cabeza))
            conexion.commit()
            messagebox.showinfo("Correcto", "Encuesta ingresada")
            mostrar_encuestas()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"No se puede ingresar la encuesta: {err}")
        finally:
            cursor.close()
            conexion.close()

# Función para mostrar encuestas
def mostrar_encuestas():
    conexion = conectar_db()
    if conexion:
        cursor = conexion.cursor()
        try:
            lista_encuestas.delete(0, tk.END)
            cursor.execute("SELECT * FROM ENCUESTA")
            for encuesta in cursor.fetchall():
                lista_encuestas.insert(tk.END, encuesta)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"No se pueden mostrar las encuestas: {err}")
        finally:
            cursor.close()
            conexion.close()

# Función para mostrar los datos de encuesta en los campos de texto
def seleccionar_encuesta(event):
    try:
        indice = lista_encuestas.curselection()[0]
        encuesta = lista_encuestas.get(indice)
        entry_id.config(state=tk.NORMAL)
        entry_id.delete(0, tk.END)
        entry_id.insert(tk.END, encuesta[0])
        entry_id.config(state=tk.DISABLED)
        entry_edad.delete(0, tk.END)
        entry_edad.insert(tk.END, encuesta[1])
        entry_sexo.delete(0, tk.END)
        entry_sexo.insert(tk.END, encuesta[2])
        entry_bebidas_semana.delete(0, tk.END)
        entry_bebidas_semana.insert(tk.END, encuesta[3])
        entry_cervezas_semana.delete(0, tk.END)
        entry_cervezas_semana.insert(tk.END, encuesta[4])
        entry_bebidas_fin_semana.delete(0, tk.END)
        entry_bebidas_fin_semana.insert(tk.END, encuesta[5])
        entry_bebidas_destiladas_semana.delete(0, tk.END)
        entry_bebidas_destiladas_semana.insert(tk.END, encuesta[6])
        entry_vinos_semana.delete(0, tk.END)
        entry_vinos_semana.insert(tk.END, encuesta[7])
        entry_perdidas_control.delete(0, tk.END)
        entry_perdidas_control.insert(tk.END, encuesta[8])
        entry_diversion_dependencia_alcohol.delete(0, tk.END)
        entry_diversion_dependencia_alcohol.insert(tk.END, encuesta[9])
        entry_problemas_digestivos.delete(0, tk.END)
        entry_problemas_digestivos.insert(tk.END, encuesta[10])
        entry_tension_alta.delete(0, tk.END)
        entry_tension_alta.insert(tk.END, encuesta[11])
        entry_dolor_cabeza.delete(0, tk.END)
        entry_dolor_cabeza.insert(tk.END, encuesta[12])
    except IndexError:
        pass

# Función para actualizar una encuesta
def actualizar_encuesta():
    conexion = conectar_db()
    if conexion:
        cursor = conexion.cursor()
        id_encuesta = entry_id.get()
        edad = entry_edad.get()
        sexo = entry_sexo.get()
        bebidas_semana = entry_bebidas_semana.get()
        cervezas_semana = entry_cervezas_semana.get()
        bebidas_fin_semana = entry_bebidas_fin_semana.get()
        bebidas_destiladas_semana = entry_bebidas_destiladas_semana.get()
        vinos_semana = entry_vinos_semana.get()
        perdidas_control = entry_perdidas_control.get()
        diversion_dependencia_alcohol = entry_diversion_dependencia_alcohol.get()
        problemas_digestivos = entry_problemas_digestivos.get()
        tension_alta = entry_tension_alta.get()
        dolor_cabeza = entry_dolor_cabeza.get()
        try:
            cursor.execute("""
                UPDATE ENCUESTA SET edad=%s, Sexo=%s, BebidasSemana=%s, CervezasSemana=%s, BebidasFinSemana=%s, 
                BebidasDestiladasSemana=%s, VinosSemana=%s, PerdidasControl=%s, DiversionDependenciaAlcohol=%s, 
                ProblemasDigestivos=%s, TensionAlta=%s, DolorCabeza=%s WHERE idEncuesta=%s
            """, (edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana, bebidas_destiladas_semana, vinos_semana, perdidas_control, diversion_dependencia_alcohol, problemas_digestivos, tension_alta, dolor_cabeza, id_encuesta))
            conexion.commit()
            messagebox.showinfo("Correcto", "Encuesta actualizada correctamente")
            mostrar_encuestas()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Encuesta no actualizada: {err}")
        finally:
            cursor.close()
            conexion.close()

# Función para eliminar una encuesta
def eliminar_encuesta():
    conexion = conectar_db()
    if conexion:
        cursor = conexion.cursor()
        id_encuesta = entry_id.get()
        try:
            cursor.execute("DELETE FROM ENCUESTA WHERE idEncuesta=%s", (id_encuesta,))
            conexion.commit()
            messagebox.showinfo("Correcto", "Encuesta eliminada correctamente")
            mostrar_encuestas()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Encuesta no eliminada: {err}")
        finally:
            cursor.close()
            conexion.close()

# Función para limpiar los campos de texto
def limpiar_campos():
    entry_id.config(state=tk.NORMAL)
    entry_id.delete(0, tk.END)
    entry_id.config(state=tk.DISABLED)
    entry_edad.delete(0, tk.END)
    entry_sexo.delete(0, tk.END)
    entry_bebidas_semana.delete(0, tk.END)
    entry_cervezas_semana.delete(0, tk.END)
    entry_bebidas_fin_semana.delete(0, tk.END)
    entry_bebidas_destiladas_semana.delete(0, tk.END)
    entry_vinos_semana.delete(0, tk.END)
    entry_perdidas_control.delete(0, tk.END)
    entry_diversion_dependencia_alcohol.delete(0, tk.END)
    entry_problemas_digestivos.delete(0, tk.END)
    entry_tension_alta.delete(0, tk.END)
    entry_dolor_cabeza.delete(0, tk.END)

# Función para graficar datos en un gráfico de líneas
def graficar_linea():
    conexion = conectar_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT idEncuesta, BebidasSemana FROM ENCUESTA")
        datos = cursor.fetchall()
        conexion.close()

        ids = [dato[0] for dato in datos]
        bebidas = [dato[1] for dato in datos]

        plt.figure(figsize=(10, 5))
        plt.plot(ids, bebidas, marker='o', linestyle='-', color='b')
        plt.title('Consumo de Bebidas por Semana')
        plt.xlabel('ID Encuesta')
        plt.ylabel('Bebidas por Semana')
        plt.grid(True)
        plt.show()

# Función para graficar datos en un gráfico circular
def graficar_pie():
    conexion = conectar_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT Sexo, COUNT(*) FROM ENCUESTA GROUP BY Sexo")
        datos = cursor.fetchall()
        conexion.close()

        etiquetas = [dato[0] for dato in datos]
        cantidades = [dato[1] for dato in datos]

        plt.figure(figsize=(8, 8))
        plt.pie(cantidades, labels=etiquetas, autopct='%1.1f%%', startangle=140)
        plt.title('Distribución por Sexo')
        plt.axis('equal')
        plt.show()

# Función para graficar datos en un gráfico de barras
def graficar_barras():
    conexion = conectar_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT idEncuesta, CervezasSemana FROM ENCUESTA")
        datos = cursor.fetchall()
        conexion.close()

        ids = [dato[0] for dato in datos]
        cervezas = [dato[1] for dato in datos]

        plt.figure(figsize=(10, 5))
        plt.bar(ids, cervezas, color='g')
        plt.title('Consumo de Cervezas por Semana')
        plt.xlabel('ID Encuesta')
        plt.ylabel('Cervezas por Semana')
        plt.grid(True)
        plt.show()

# Función para exportar datos a Excel
def exportar_excel():
    conexion = conectar_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM ENCUESTA")
        datos = cursor.fetchall()
        conexion.close()

        # Crear DataFrame de pandas
        df = pd.DataFrame(datos, columns=[
            'idEncuesta', 'edad', 'Sexo', 'BebidasSemana', 'CervezasSemana', 
            'BebidasFinSemana', 'BebidasDestiladasSemana', 'VinosSemana', 
            'PerdidasControl', 'DiversionDependenciaAlcohol', 'ProblemasDigestivos', 
            'TensionAlta', 'DolorCabeza'
        ])

        # Exportar a archivo Excel
        archivo_excel = 'encuestas_exportadas.xlsx'
        df.to_excel(archivo_excel, index=False)
        messagebox.showinfo("Exportación Exitosa", f"Datos exportados a {archivo_excel} correctamente")

# Crear ventana con título
ventana = tk.Tk()
ventana.title("Gestión de Encuestas")

# Menú
menu_bar = tk.Menu(ventana)
ventana.config(menu=menu_bar)
menu_archivo = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Nuevo", command=limpiar_campos)
menu_archivo.add_command(label="Salir", command=ventana.quit)

# Campos
tk.Label(ventana, text="ID Encuesta: ").grid(row=0, column=0)
entry_id = tk.Entry(ventana, state=tk.DISABLED)
entry_id.grid(row=0, column=1)

tk.Label(ventana, text="Edad: ").grid(row=1, column=0)
entry_edad = tk.Entry(ventana)
entry_edad.grid(row=1, column=1)

tk.Label(ventana, text="Sexo: ").grid(row=2, column=0)
entry_sexo = tk.Entry(ventana)
entry_sexo.grid(row=2, column=1)

tk.Label(ventana, text="Bebidas por Semana: ").grid(row=3, column=0)
entry_bebidas_semana = tk.Entry(ventana)
entry_bebidas_semana.grid(row=3, column=1)

tk.Label(ventana, text="Cervezas por Semana: ").grid(row=4, column=0)
entry_cervezas_semana = tk.Entry(ventana)
entry_cervezas_semana.grid(row=4, column=1)

tk.Label(ventana, text="Bebidas Fin de Semana: ").grid(row=5, column=0)
entry_bebidas_fin_semana = tk.Entry(ventana)
entry_bebidas_fin_semana.grid(row=5, column=1)

tk.Label(ventana, text="Bebidas Destiladas por Semana: ").grid(row=6, column=0)
entry_bebidas_destiladas_semana = tk.Entry(ventana)
entry_bebidas_destiladas_semana.grid(row=6, column=1)

tk.Label(ventana, text="Vinos por Semana: ").grid(row=7, column=0)
entry_vinos_semana = tk.Entry(ventana)
entry_vinos_semana.grid(row=7, column=1)

tk.Label(ventana, text="Pérdidas de Control: ").grid(row=8, column=0)
entry_perdidas_control = tk.Entry(ventana)
entry_perdidas_control.grid(row=8, column=1)

tk.Label(ventana, text="Diversión Dependencia Alcohol: ").grid(row=9, column=0)
entry_diversion_dependencia_alcohol = tk.Entry(ventana)
entry_diversion_dependencia_alcohol.grid(row=9, column=1)

tk.Label(ventana, text="Problemas Digestivos: ").grid(row=10, column=0)
entry_problemas_digestivos = tk.Entry(ventana)
entry_problemas_digestivos.grid(row=10, column=1)

tk.Label(ventana, text="Tensión Alta: ").grid(row=11, column=0)
entry_tension_alta = tk.Entry(ventana)
entry_tension_alta.grid(row=11, column=1)

tk.Label(ventana, text="Dolor de Cabeza: ").grid(row=12, column=0)
entry_dolor_cabeza = tk.Entry(ventana)
entry_dolor_cabeza.grid(row=12, column=1)

# Botones
tk.Button(ventana, text="Ingresar", command=crear_encuesta, bg="blue", fg="white").grid(row=13, column=0)
tk.Button(ventana, text="Actualizar", command=actualizar_encuesta, bg="green", fg="white").grid(row=13, column=1)
tk.Button(ventana, text="Eliminar", command=eliminar_encuesta, bg="red", fg="white").grid(row=14, column=0)
tk.Button(ventana, text="Nuevo", command=limpiar_campos, bg="orange", fg="white").grid(row=14, column=1)

# Lista de encuestas
lista_encuestas = tk.Listbox(ventana, width=100)
lista_encuestas.grid(row=15, column=0, columnspan=2)
lista_encuestas.bind("<<ListboxSelect>>", seleccionar_encuesta)

# Botones para mostrar gráficos
tk.Button(ventana, text="Gráfico de Línea", command=graficar_linea, bg="purple", fg="white").grid(row=16, column=0)
tk.Button(ventana, text="Gráfico Circular", command=graficar_pie, bg="purple", fg="white").grid(row=16, column=1)
tk.Button(ventana, text="Gráfico de Barras", command=graficar_barras, bg="purple", fg="white").grid(row=17, column=0)
tk.Button(ventana, text="Exportar a Excel", command=exportar_excel, bg="cyan", fg="black").grid(row=17, column=1)

# Mostrar encuestas al iniciar
mostrar_encuestas()

ventana.mainloop()