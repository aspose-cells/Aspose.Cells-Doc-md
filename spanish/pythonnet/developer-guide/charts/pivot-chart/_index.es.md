---
title: Cómo agregar un PivotChart usando Aspose.Cells para Python via .NET
linktitle: Gráfico de Tabla Dinámica
type: docs
weight: 100
url: /es/python-net/how-to-add-pivot-chart/
description: Cómo agregar un PivotChart usando Aspose.Cells para Python via .NET.
keywords: PivotChart
---
## ¿Qué es un PivotChart?

Un gráfico dinámico es una representación visual de los datos en una tabla dinámica. Los gráficos dinámicos ofrecen una forma de resumir, analizar, explorar y presentar datos resumidos. Aquí algunas características clave y aspectos de los gráficos dinámicos:

1. Representación dinámica de datos: Los gráficos dinámicos se actualizan automáticamente para reflejar cambios en la tabla dinámica. Si añades o eliminas campos en la tabla dinámica, el gráfico dinámico se actualiza en consecuencia.

1. Interactivo: Los gráficos dinámicos son interactivos, permitiendo a los usuarios filtrar, ordenar y profundizar en los datos. Esto facilita explorar diferentes aspectos del conjunto de datos.

1. Diseño flexible: Los usuarios pueden cambiar el diseño del gráfico dinámico arrastrando y soltando campos, lo que ofrece flexibilidad en la visualización de datos.

1. Diversos tipos de gráficos: Los gráficos dinámicos se pueden crear usando varios tipos de gráficos, como barras, líneas, tartas y más, dependiendo de la naturaleza de los datos y las ideas que deseas obtener.

1. Resumen: Los gráficos dinámicos resumen grandes cantidades de datos y pueden mostrar totales, promedios, conteos u otras estadísticas resumidas.

1. Filtrado: Proporcionan capacidades de filtrado, permitiendo mostrar solo los datos que cumplen ciertos criterios.

<br>
Los gráficos dinámicos se usan comúnmente en inteligencia empresarial y análisis de datos para ofrecer un resumen visual claro y conciso de conjuntos de datos complejos. Son una herramienta poderosa para tomar decisiones basadas en datos.

## Cómo agregar un gráfico dinámico usando la biblioteca Aspose.Cells para Python Excel

### **Añadiendo una tabla dinámica**

Para crear una tabla dinámica utilizando Aspose.Cells para Python via .NET:

1. Agregue algunos datos a las celdas de una hoja de cálculo utilizando el método PutValue/setValue de un objeto Cell. También puede utilizar un archivo de plantilla ya lleno con datos. Los datos se utilizarán como origen de datos de la tabla dinámica.
1. Agregue una tabla dinámica a la hoja de cálculo llamando al método add de la colección PivotTables (encapsulada en el objeto Worksheet).
1. Accede al nuevo objeto PivotTable desde la colección PivotTables pasando su índice. # Usa cualquiera de los objetos de tabla dinámica encapsulados en el objeto PivotTable para gestionar la tabla.

A continuación se muestran ejemplos de código.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreatePivotTable-1.py" >}}

### **Añadiendo un gráfico dinámico**

Para crear un PivotChart utilizando Aspose.Cells para Python via .NET:

1. Agregue un gráfico.
1. Establezca el PivotSource del gráfico para hacer referencia a una tabla dinámica existente en la hoja de cálculo.
1. Establezca otros atributos.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreatePivotChart-1.py" >}}

