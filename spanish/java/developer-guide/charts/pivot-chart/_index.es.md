---
title: Cómo agregar un gráfico dinámico usando Aspose.Cells
linktitle: Gráfico dinámico
type: docs
weight: 100
url: /es/java/how-to-add-pivot-chart/
description: Cómo agregar un gráfico dinámico usando Aspose.Cells.
keywords: PivotChart
---
##  ¿Qué es el gráfico dinámico?

Un gráfico dinámico en Excel es una representación gráfica de datos creados a partir de una tabla dinámica. Permite a los usuarios visualizar y analizar datos dinámicamente resumiendo y mostrando información en forma de gráfico. Los gráficos dinámicos son interactivos y se pueden modificar fácilmente para mostrar diferentes perspectivas de los datos, lo que los convierte en una poderosa herramienta para el análisis y la presentación de datos en Excel.

##  Cómo agregar un gráfico dinámico usando Aspose.Cells
###  **Crear una tabla dinámica**

Para crear una tabla dinámica usando Aspose.Cells:

1. Agregue algunos datos a las celdas de una hoja de trabajo utilizando el método PutValue/setValue de un objeto Cell. También utiliza un archivo de plantilla ya lleno de datos. Los datos se utilizarán como fuente de datos de la tabla dinámica.
1. Agregue una tabla dinámica a la hoja de trabajo llamando al método add de la colección PivotTables (encapsulado en el objeto Hoja de trabajo).
1. Acceda al nuevo objeto de tabla dinámica de la colección de tablas dinámicas pasando su índice.
1. Utilice cualquiera de los objetos de tabla dinámica encapsulados en el objeto Tabla dinámica para administrar la tabla.

A continuación se proporciona un ejemplo de código. La ejecución del código genera un nuevo archivo: pivotTable_test.xls.

**Datos de entrada** 

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_1.png)

**La tabla dinámica de salida**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

###  **Crear un gráfico dinámico basado en la tabla dinámica**

Para crear un gráfico dinámico usando Aspose.Cells:

1. Añade un gráfico.
1. Establezca el PivotSource del gráfico para que haga referencia a una tabla dinámica existente en la hoja de cálculo.
1. Establece otros atributos.

A continuación se muestra el código utilizado por el componente para realizar la tarea. La ejecución del código genera un nuevo archivo: pivotChart_test.xls.

**La hoja del gráfico dinámico**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

Este artículo muestra cómo crear tablas dinámicas y gráficos dinámicos usando Aspose.Cells. Con suerte, le ayudará a utilizar estas funciones en sus propios escenarios.

Aspose.Cells se ha beneficiado de años de investigación, diseño y cuidadosa puesta a punto.

 Agradecemos sus consultas, comentarios y sugerencias en[Aspose.Cells Foro](https://forum.aspose.com/c/cells/9). Garantizamos una pronta respuesta.

{{% /alert %}}
