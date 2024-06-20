---
title: Tres métodos para filtrar datos de gráficos
description: Aprende a filtrar gráficos en Excel usando Aspose.Cells for .NET. Nuestra guía completa te mostrará cómo aplicar filtros a gráficos, personalizar elementos del gráfico y utilizar herramientas de análisis de datos para obtener mejores ideas y tomar decisiones informadas.
keywords: Aspose.Cells for .NET, Filtrado de gráficos en Excel, Análisis de datos, Toma de decisiones, Visualización
type: docs
weight: 2210
url: /es/net/filtering-charts-in-excel/
---

{{% alert color="primary" %}}

## **1. Filtrado de series para representar un gráfico**

### **Pasos para filtrar series de un gráfico en Excel**
En Excel, podemos filtrar series específicas de un gráfico, lo que hace que esas series filtradas no se muestren en el gráfico. El gráfico original se muestra en **Figura 1**. Sin embargo, cuando filtramos **Testseries2** y **Testseries4**, el gráfico aparecerá como se muestra en **Figura 2**.

En Aspose.Cells, podemos realizar una operación similar. Para un archivo de [muestra](seriesFiltered.xlsx) como este, si queremos filtrar **Testseries2** y **Testseries4**, podemos ejecutar el siguiente código. Además, mantendremos dos listas: una lista ([NSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/)) para almacenar todas las series seleccionadas y otra ([FilteredNSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filteredSeries/)) para almacenar las series filtradas.

Por favor, **nota** que en el código, cuando establecemos **chart.NSeries[0].IsFiltered = true;**, la primera serie en [NSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/) se eliminará y se colocará en la posición correspondiente dentro de [FilteredNSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filteredSeries/). Posteriormente, la anterior **NSeries[1]** se convertirá en el nuevo primer elemento en la lista, y todas las series siguientes se desplazarán hacia adelante en una posición. Esto significa que si luego ejecutamos **chart.NSeries[1].IsFiltered = true;**, estaremos eliminando efectivamente la tercera serie original. Esto a veces puede causar confusión, por lo que recomendamos seguir la operación en el código, que elimina las series desde el final hasta el principio.

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **Código de muestra**
El siguiente código de muestra carga el [archivo de Excel de muestra](seriesFiltered.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "seriesFiltered.cs" >}}

## **2. Filtra los datos y permite que el gráfico cambie**

Filtrar tus datos es una excelente manera de manejar los filtros de gráficos con muchos datos. Cuando filtras los datos, el gráfico cambiará. Un problema que tendremos que abordar es asegurarnos de que el gráfico permanezca en la pantalla. Cuando filtras, obtienes filas ocultas y, ocasionalmente, el gráfico estará en esas filas ocultas.

![todo:image_alt_text](Figure3.png)

### **Pasos para utilizar los Filtros de Datos para cambiar el gráfico en Excel**

1. Haz clic dentro de tu rango de datos.
2. Haz clic en la pestaña **Datos** y activa los Filtros haciendo clic en Filtros. Tu fila de encabezado tendrá flechas desplegables.
3. Crea un gráfico yendo a la pestaña **Insertar** y seleccionando un gráfico de columnas.
4. Ahora filtra tus datos usando las flechas desplegables en los datos. No uses los Filtros de Gráfico.

### **Código de muestra**
El siguiente código de muestra muestra la misma característica usando Aspsoe.Cells.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DataFilters.cs" >}}

## **3. Filtra los datos utilizando una Tabla y permite que el gráfico cambie**

Utilizar una Tabla es similar al Método 2, utilizando un rango, pero tienes ventajas con las tablas sobre los rangos. Cuando cambias tu rango a una Tabla y agregas datos, el gráfico se actualiza automáticamente. Con un rango, tendrás que cambiar la fuente de datos.

### **Formatear como tabla en Excel**

Haz clic dentro de tus datos y usa **CTRL + T** o ve a la pestaña Inicio, **Formato como Tabla**

![todo:image_alt_text](Figure4.png)

### **Código de muestra**
El siguiente código de muestra carga el [archivo de Excel de muestra](TableFilters.xlsx) muestra la misma característica usando Aspsoe.Cells.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "TableFilters.cs" >}}
