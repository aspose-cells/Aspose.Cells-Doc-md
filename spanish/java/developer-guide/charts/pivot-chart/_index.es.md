---
title: Cómo agregar un PivotChart usando Aspose.Cells
linktitle: Gráfico de Tabla Dinámica
type: docs
weight: 100
url: /es/java/how-to-add-pivot-chart/
description: Cómo agregar un PivotChart usando Aspose.Cells.
keywords: PivotChart
---
## ¿Qué es un PivotChart?

Un PivotChart en Excel es una representación gráfica de datos creada a partir de una tabla dinámica. Permite a los usuarios visualizar y analizar datos de forma dinámica resumiendo y mostrando información en forma de gráfico. Los PivotCharts son interactivos y pueden modificarse fácilmente para mostrar diferentes perspectivas de los datos, convirtiéndolo en una poderosa herramienta para el análisis y la presentación de datos en Excel.

## Cómo agregar un PivotChart usando Aspose.Cells
### **Crear una tabla dinámica**

Para crear una tabla dinámica usando Aspose.Cells:

1. Agregue algunos datos a las celdas de una hoja de cálculo utilizando el método PutValue/setValue de un objeto Cell. También puede utilizar un archivo de plantilla ya lleno con datos. Los datos se utilizarán como origen de datos de la tabla dinámica.
1. Agregue una tabla dinámica a la hoja de cálculo llamando al método add de la colección PivotTables (encapsulada en el objeto Worksheet).
1. Acceda al nuevo objeto PivotTable de la colección PivotTables pasando su índice.
1. Utilice cualquiera de los objetos de tabla dinámica encapsulados en el objeto PivotTable para administrar la tabla.

A continuación se muestra un ejemplo de código. La ejecución del código genera un nuevo archivo: pivotTable_test.xls.

**Datos de entrada** 

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_1.png)

**La tabla dinámica de salida**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

### **Crear un gráfico dinámico basado en la tabla dinámica**

Para crear un gráfico dinámico usando Aspose.Cells:

1. Agregue un gráfico.
1. Establezca el PivotSource del gráfico para hacer referencia a una tabla dinámica existente en la hoja de cálculo.
1. Establezca otros atributos.

A continuación se muestra el código utilizado por el componente para realizar la tarea. Al ejecutar el código se genera un nuevo archivo: pivotChart_test.xls.

**La hoja del gráfico dinámico**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

Este artículo muestra cómo crear tablas dinámicas y gráficos dinámicos utilizando Aspose.Cells. Con suerte, le ayudará a usar estas características en sus propios escenarios.

Aspose.Cells se ha beneficiado de años de investigación, diseño y ajustes cuidadosos.

Agradecemos sus consultas, comentarios y sugerencias en el [Foro de Aspose.Cells](https://forum.aspose.com/c/cells/9). Garantizamos una pronta respuesta.

{{% /alert %}}
