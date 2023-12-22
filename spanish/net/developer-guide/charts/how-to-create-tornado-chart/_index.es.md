---
title: Cómo crear un gráfico de tornado
type: docs
weight: 73
url: /es/net/create-tornado-chart/
description: Aprenda a crear un gráfico de tornado con Aspose.Cells for .NET API.
keywords: C# create a tornado chart, add a tornado chart, insert a tornado chart
---
##  **Introducción**
Un gráfico de tornado, también conocido como diagrama de tornado o gráfico de tornado, es un tipo de visualización de datos que se utiliza a menudo para el análisis de sensibilidad en Excel. Le ayuda a comprender el impacto del cambio de variables en un resultado o resultado particular.

##  **Cómo crear un gráfico de tornado en Excel**
Puede crear un gráfico de tornado en Excel siguiendo estos pasos:
1. Seleccione los datos y vaya a Insertar --> Gráficos --> Insertar gráfico de columnas o barras --> Gráfico de barras apiladas. Haz click en eso.
<br>
<img src="1.png" width=70% />
2. Cambie el eje Y: haga clic derecho en el eje y. Haga clic en el eje de formato. En etiquetas, haga clic en el menú desplegable de posición de la etiqueta y seleccione el elemento Bajo.
<br>
<img src="2.png" width=70% />
3. Seleccione cualquier barra y vaya a formato. Establezca un ancho de espacio apropiado.
<br>
<img src="3.png" width=70% />
4. Eliminemos el signo menos (-) del gráfico de tornados. Seleccione el eje x. Ir a formateo. En las opciones del eje, haga clic en el número. En categoría, seleccione personalizado. En el código de formato escriba ###0,###0. Haga clic en agregar.
<br>
<img src="4.png" width=70% />
5. haga clic en el eje y y vaya a las opciones del eje. En las opciones de Eje, marque Categorías en orden inverso.
<br>
<img src="5.png" width=70% />

##  **Cómo agregar un gráfico de tornado en Aspose.Cells**
 Consulte el siguiente código de muestra. Se carga el[archivo de Excel de muestra](sample.xlsx) que contiene algunos datos de muestra. Luego crea el gráfico de barras apiladas basándose en los datos iniciales y establece las propiedades relevantes. Finalmente, guarda el libro de trabajo en[formato de salida XLSX](out.xlsx). La siguiente captura de pantalla muestra el gráfico de tornado creado por Aspose.Cells en el archivo Excel de salida.
<br>
<img src="6.png" width=70% />

###  **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-tornado-chart.cs" >}}