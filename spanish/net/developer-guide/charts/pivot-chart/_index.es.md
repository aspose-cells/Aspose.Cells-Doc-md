---
title: Cómo agregar un gráfico dinámico usando Aspose.Cells
linktitle: Gráfico dinámico
type: docs
weight: 100
url: /es/net/how-to-add-pivot-chart/
description: Cómo agregar un gráfico dinámico usando Aspose.Cells.
keywords: PivotChart
---
##  ¿Qué es el gráfico dinámico?

Un gráfico dinámico en Excel es una representación gráfica de datos creados a partir de una tabla dinámica. Permite a los usuarios visualizar y analizar datos dinámicamente resumiendo y mostrando información en forma de gráfico. Los gráficos dinámicos son interactivos y se pueden modificar fácilmente para mostrar diferentes perspectivas de los datos, lo que los convierte en una poderosa herramienta para el análisis y la presentación de datos en Excel.

##  Cómo agregar un gráfico dinámico usando Aspose.Cells

###  **Agregar una tabla dinámica**

Para crear una tabla dinámica usando Aspose.Cells:

1. Agregue algunos datos a las celdas de una hoja de trabajo utilizando el método PutValue/setValue de un objeto Cell. También utiliza un archivo de plantilla ya lleno de datos. Los datos se utilizarán como fuente de datos de la tabla dinámica.
1. Agregue una tabla dinámica a la hoja de trabajo llamando al método add de la colección PivotTables (encapsulado en el objeto Hoja de trabajo).
1. Acceda al nuevo objeto de tabla dinámica de la colección de tablas dinámicas pasando su índice. # Utilice cualquiera de los objetos de la tabla dinámica encapsulados en el objeto PivotTable para administrar la tabla.

A continuación se proporcionan ejemplos de código.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

###  **Agregar un gráfico dinámico**

Para crear un gráfico dinámico usando Aspose.Cells:

1. Añade un gráfico.
1. Establezca el PivotSource del gráfico para que haga referencia a una tabla dinámica existente en la hoja de cálculo.
1. Establece otros atributos.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

