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

Un gráfico dinámico es una representación visual de los datos en una tabla dinámica. Los gráficos dinámicos proporcionan una forma de resumir, analizar, explorar y presentar datos de resumen. Aquí hay algunas características clave y aspectos de los gráficos dinámicos:

1. Representación dinámica de datos: los gráficos dinámicos se actualizan automáticamente para reflejar cambios en la tabla dinámica. Si agrega o elimina campos en la tabla dinámica, el gráfico dinámico se actualiza en consecuencia.

1. Interactivo: los gráficos dinámicos son interactivos, lo que permite a los usuarios filtrar, ordenar y profundizar en los datos. Esto facilita explorar diferentes aspectos del conjunto de datos.

1. Diseño flexible: los usuarios pueden cambiar el diseño del gráfico dinámico arrastrando y soltando campos, lo que ofrece flexibilidad en la visualización de datos.

1. Varios tipos de gráficos: los gráficos dinámicos se pueden crear utilizando varios tipos de gráficos como gráficos de barras, gráficos de líneas, gráficos circulares, y más, dependiendo de la naturaleza de los datos y las ideas que desee obtener.

1. Resumen: los gráficos dinámicos resumen grandes cantidades de datos y pueden mostrar totales, promedios, recuentos u otras estadísticas de resumen.

1. Filtrado: proporcionan capacidades de filtrado, lo que le permite mostrar solo los datos que cumplen ciertos criterios.

<br>
Los gráficos dinámicos se utilizan comúnmente en inteligencia empresarial y análisis de datos para proporcionar un resumen visual claro y conciso de conjuntos de datos complejos. Son una herramienta poderosa para tomar decisiones basadas en datos.

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

