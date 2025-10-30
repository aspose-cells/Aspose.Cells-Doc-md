---
title: Cómo crear un gráfico de tornado con Golang a través de C++
linktitle: Crear gráfico de tornado
type: docs
weight: 73
url: /es/go-cpp/create-tornado-chart/
description: Aprende cómo crear un gráfico de tornado con la API Aspose.Cells for C++.
keywords: C++ crea un gráfico de tornado, agrega un gráfico de tornado, inserta un gráfico de tornado
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
5. Haz clic en el eje y y ve a las opciones del eje. En las opciones del eje, marca Categorías en orden inverso.
<br>
<img src="5.png" width=70% />

## **Cómo agregar un gráfico tornado en Aspose.Cells**
Por favor, consulta el siguiente código de muestra. Carga el [archivo de Excel de muestra](sample.xlsx) que contiene algunos datos de ejemplo. Luego, crea el gráfico de barras apiladas basado en los datos iniciales y establece propiedades relevantes. Finalmente, guarda el libro de trabajo en [formato XLSX de salida](out.xlsx). La siguiente captura de pantalla muestra el gráfico tornado creado por Aspose.Cells en el archivo de Excel de salida.
<br>
<img src="6.png" width=70% />

### **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToCreateTornadoChart.go" >}}
