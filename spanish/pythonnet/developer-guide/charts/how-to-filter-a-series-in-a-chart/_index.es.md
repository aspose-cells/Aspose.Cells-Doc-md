---
title: Tres métodos para filtrar datos de gráficos
description: Aprenda cómo filtrar gráficos en Excel usando Aspose.Cells para Python via .NET. Nuestra guía completa demostrará cómo aplicar filtros a los gráficos, personalizar los elementos del gráfico y usar herramientas de análisis de datos para obtener mejores ideas y tomar decisiones informadas.
keywords: Aspose.Cells para Python via .NET, Filtrado de gráficos en Excel, Análisis de datos, Toma de decisiones, Visualización.
type: docs
weight: 2210
url: /es/python-net/filtering-charts-in-excel/
---


## **1. Filtrado de series para representar un gráfico**

### **Pasos para filtrar series de un gráfico en Excel**
En Excel, podemos filtrar series específicas de un gráfico, lo que hace que esas series filtradas no se muestren en el gráfico. El gráfico original se muestra en **Figura 1**. Sin embargo, cuando filtramos **Testseries2** y **Testseries4**, el gráfico aparecerá como se muestra en **Figura 2**.

En Aspose.Cells para Python via .NET, podemos realizar una operación similar. Para un [archivo de ejemplo](seriesFiltered.xlsx) como este, si queremos filtrar **Testseries2** y **Testseries4**, podemos ejecutar el siguiente código. Además, mantendremos dos listas: una ([n_series](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/n_series/)) para almacenar todas las series seleccionadas y otra ([filtered_n_series](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/filtered_n_series/)) para almacenar las series filtradas.

Por favor, **tenga en cuenta** que en el código, cuando establecemos **chart.nSeries[0].is_filtered = TRUE;**, la primera serie en [n_series](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/n_series/) será eliminada y colocada en la posición correspondiente dentro de [filtered_n_series](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/filtered_n_series/). Posteriormente, el anterior **nSeries[1]** se convertirá en el nuevo primer ítem en la lista, y todas las series siguientes se desplazarán hacia adelante en una posición. Esto significa que si luego ejecutamos **chart.nSeries[1].is_filtered = TRUE;**, estamos eliminando efectivamente la serie original en la tercera posición. Esto puede llevar a confusión, por lo que recomendamos seguir la operación en el código, que elimina las series desde el final hasta el principio.

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **Código de muestra**
El siguiente código de muestra carga el [archivo de Excel de muestra](seriesFiltered.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-seriesFiltered.py" >}}

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-DataFilters.py" >}}

## **3. Filtra los datos utilizando una Tabla y permite que el gráfico cambie**

Utilizar una Tabla es similar al Método 2, utilizando un rango, pero tienes ventajas con las tablas sobre los rangos. Cuando cambias tu rango a una Tabla y agregas datos, el gráfico se actualiza automáticamente. Con un rango, tendrás que cambiar la fuente de datos.

### **Formatear como tabla en Excel**

Haz clic dentro de tus datos y usa **CTRL + T** o ve a la pestaña Inicio, **Formato como Tabla**

![todo:image_alt_text](Figure4.png)

### **Código de muestra**
El siguiente código de muestra carga el [archivo de Excel de muestra](TableFilters.xlsx) muestra la misma característica usando Aspsoe.Cells.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-TableFilters.py" >}}
{{< app/cells/assistant language="python-net" >}}
