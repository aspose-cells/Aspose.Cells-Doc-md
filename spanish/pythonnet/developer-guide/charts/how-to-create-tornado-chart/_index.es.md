---
title: Cómo crear un gráfico de tornado
type: docs
weight: 73
url: /es/python-net/create-tornado-chart/
description: Aprenda cómo crear un gráfico de tornado con Aspose.Cells para Python via .NET API.
keywords: Crear un gráfico de tornado en Python, agregar un gráfico de tornado, insertar un gráfico de tornado
---

## **Introducción**
Un gráfico tornado, también conocido como diagrama tornado o gráfico tornado, es un tipo de visualización de datos que se utiliza a menudo para análisis de sensibilidad en Excel. Te ayuda a comprender el impacto de cambiar variables en un resultado particular.

## **Cómo crear un gráfico tornado en Excel**
Puedes crear un gráfico tornado en Excel siguiendo estos pasos:
1. Selecciona los datos y ve a Insertar --> Gráficos --> Insertar gráfico de columnas o barras --> Gráfico de barras apiladas. Haz clic en él.
<br>
<img src="1.png" width=70% />
2. Cambia el eje Y: Haz clic derecho en el eje Y. Haz clic en formato de eje. En etiquetas, haz clic en posición de la etiqueta desplegable y selecciona elemento inferior.
<br>
<img src="2.png" width=70% />
3. Selecciona cualquier barra y ve a formato. Establece un ancho de espacio adecuado.
<br>
<img src="3.png" width=70% />
4. Vamos a quitar el signo menos (-) del gráfico tornado. Selecciona el eje X. Ve a formato. En las opciones del eje, haz clic en el número. En categoría, selecciona personalizado. En código de formato escribe ###0,###0. Haz clic en añadir.
<br>
<img src="4.png" width=70% />
5. haz clic en el eje Y y ve a las opciones del eje. En las opciones del eje, marca Categorías en orden inverso.
<br>
<img src="5.png" width=70% />

## **Cómo agregar un gráfico de tornado en la Biblioteca de Excel Aspose.Cells para Python**
Por favor, vea el siguiente código de ejemplo. Carga el [archivo Excel de ejemplo](sample.xlsx) que contiene algunos datos de muestra. Luego crea el gráfico de barras apiladas basado en los datos iniciales y establece las propiedades relevantes. Finalmente, guarda el libro de trabajo en [formato XLSX de salida](out.xlsx). La siguiente captura de pantalla muestra el gráfico de tornado creado por Aspose.Cells para Python via .NET en el archivo Excel de salida.
<br>
<img src="6.png" width=70% />

### **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-create-tornado-chart.py" >}}
{{< app/cells/assistant language="python-net" >}}
