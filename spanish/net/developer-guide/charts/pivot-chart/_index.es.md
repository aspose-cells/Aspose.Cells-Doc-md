---
title: Cómo agregar un PivotChart usando Aspose.Cells
linktitle: Gráfico de Tabla Dinámica
type: docs
weight: 100
url: /es/net/how-to-add-pivot-chart/
description: Cómo agregar un PivotChart usando Aspose.Cells.
keywords: PivotChart
---
## ¿Qué es un PivotChart?

Un PivotChart en Excel es una representación gráfica de datos creada a partir de una tabla dinámica. Permite a los usuarios visualizar y analizar datos de forma dinámica resumiendo y mostrando información en forma de gráfico. Los PivotCharts son interactivos y pueden modificarse fácilmente para mostrar diferentes perspectivas de los datos, convirtiéndolo en una poderosa herramienta para el análisis y la presentación de datos en Excel.

## Cómo agregar un PivotChart usando Aspose.Cells

### **Añadiendo una tabla dinámica**

Para crear una tabla dinámica usando Aspose.Cells:

1. Agregue algunos datos a las celdas de una hoja de cálculo utilizando el método PutValue/setValue de un objeto Cell. También puede utilizar un archivo de plantilla ya lleno con datos. Los datos se utilizarán como origen de datos de la tabla dinámica.
1. Agregue una tabla dinámica a la hoja de cálculo llamando al método add de la colección PivotTables (encapsulada en el objeto Worksheet).
1. Accede al nuevo objeto PivotTable desde la colección PivotTables pasando su índice. # Usa cualquiera de los objetos de tabla dinámica encapsulados en el objeto PivotTable para gestionar la tabla.

A continuación se muestran ejemplos de código.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

### **Añadiendo un gráfico dinámico**

Para crear un gráfico dinámico usando Aspose.Cells:

1. Agregue un gráfico.
1. Establezca el PivotSource del gráfico para hacer referencia a una tabla dinámica existente en la hoja de cálculo.
1. Establezca otros atributos.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

