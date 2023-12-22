---
title: Tres métodos para filtrar datos de gráficos
description: Aprenda a filtrar gráficos en Excel usando Aspose.Cells for .NET. Nuestra guía completa le demostrará cómo aplicar filtros a los gráficos, personalizar elementos de los gráficos y utilizar herramientas de análisis de datos para obtener mejores conocimientos y una toma de decisiones informada.
keywords: Aspose.Cells for .NET, Filtering Charts in Excel, Data Analysis, Decision Making, Visualization.
type: docs
weight: 2210
url: /es/net/filtering-charts-in-excel/
---
{{% alert color="primary" %}}

##  **1. Filtrar series para representar un gráfico**

###  **Pasos para filtrar series de un gráfico en Excel**
 En Excel, podemos filtrar series específicas de un gráfico, lo que hace que esas series filtradas no se muestren en el gráfico. El cuadro original se muestra en**Figura 1**. Sin embargo, cuando filtramos **Testseries2** y *Testseries4**, el gráfico aparecerá como se muestra en la *Figura 2**.

 En Aspose.Cells podemos realizar una operación similar. Para[muestra](seriesFiltered.xlsx) archivo como este, si queremos filtrar**Serie de pruebas2** y *Testseries4**, podemos ejecutar el siguiente código. Además, mantendremos dos listas: una ([Serie N](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/)) lista para almacenar todas las series seleccionadas y otra ([Serie N filtrada](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filteredSeries/)) para almacenar la serie filtrada.

Por favor**nota** que en el código, cuando configuramos**chart.NSeries[0].IsFiltered = true;**, se eliminará la primera serie de [NSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/) y colocado en la posición adecuada dentro de [FilteredNSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filteredSeries/). Posteriormente, el anterior **NSeries[1]** se convertirá en el nuevo primer elemento de la lista y todas las series siguientes avanzarán una posición. Esto significa que si luego ejecutamos *chart.NSeries[1].IsFiltered = true;**, efectivamente estamos eliminando la tercera serie original. Esto a veces puede generar confusión, por lo que recomendamos seguir la operación en el código, que elimina series desde el final hasta el principio.

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

###  **Código de muestra**
 El siguiente código de muestra carga el[archivo de Excel de muestra](seriesFiltered.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "seriesFiltered.cs" >}}

##  **2. Filtra los datos y deja que el gráfico cambie.**

Filtrar sus datos es una excelente manera de manejar filtros de gráficos con una gran cantidad de datos. Cuando filtres los datos, el gráfico cambiará. Un problema que tendremos que abordar es asegurarnos de que el gráfico permanezca en la pantalla. Cuando filtra, obtiene filas ocultas y, ocasionalmente, el gráfico estará en esas filas ocultas.

![todo:image_alt_text](Figure3.png)

###  **Pasos para usar filtros de datos para cambiar el gráfico en Excel**

1. Haga clic dentro de su rango de datos.
 2. Haga clic en el**Datos** y active Filtros haciendo clic en Filtros. Su fila de encabezado tendrá flechas desplegables.
 3. Cree un gráfico yendo a**Insertar** y seleccionando un gráfico de columnas.
4. Ahora filtre sus datos usando las flechas desplegables en los datos. No utilice los filtros de gráficos.

###  **Código de muestra**
El siguiente código de muestra muestra la misma característica usando Aspsoe.Cells.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DataFilters.cs" >}}

##  **3. Filtra los datos usando una tabla y deja que el gráfico cambie.**

Usar una tabla es similar al Método 2, usar un rango, pero tiene ventajas con las tablas sobre los rangos. Cuando cambia su rango a una tabla y agrega datos, el gráfico se actualiza automáticamente. Con un rango, tendrás que cambiar la fuente de datos.

###  **Formatear como tabla en Excel**

 Haga clic dentro de sus datos y utilice**CTRL+T** o utilice la pestaña Inicio,**Formatear como tabla**

![todo:image_alt_text](Figure4.png)

###  **Código de muestra**
 El siguiente código de muestra carga el[archivo de Excel de muestra](TableFilters.xlsx) muestra la misma característica usando Aspsoe.Cells.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "TableFilters.cs" >}}