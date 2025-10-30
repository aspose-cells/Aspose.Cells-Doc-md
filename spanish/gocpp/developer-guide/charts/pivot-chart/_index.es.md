---
title: Cómo agregar un PivotChart con Golang vía C++
linktitle: Gráfico de Tabla Dinámica
type: docs
weight: 100
url: /es/go-cpp/how-to-add-pivot-chart/
description: Cómo agregar un PivotChart usando Aspose.Cells con Golang vía C++.
keywords: PivotChart
---

## ¿Qué es un PivotChart?

Un gráfico dinámico es una representación visual de los datos en una tabla dinámica. Los gráficos dinámicos ofrecen una forma de resumir, analizar, explorar y presentar datos resumidos. Aquí algunas características clave y aspectos de los gráficos dinámicos:

1. **Representación dinámica de datos**: Los gráficos dinámicos se actualizan automáticamente para reflejar cambios en la tabla dinámica. Si agregas o quitas campos en la tabla dinámica, el gráfico dinámico se actualiza en consecuencia.

1. **Interactivo**: Los gráficos dinámicos son interactivos, permitiendo a los usuarios filtrar, ordenar y profundizar en los datos. Esto facilita explorar diferentes aspectos del conjunto de datos.

1. **Diseño flexible**: Los usuarios pueden cambiar el diseño del gráfico dinámico arrastrando y soltando campos, lo que ofrece flexibilidad en la visualización de datos.

1. **Varios tipos de gráficos**: Los gráficos dinámicos pueden crearse usando varios tipos de gráficos, como barras, líneas, círculos y más, dependiendo de la naturaleza de los datos y los conocimientos que deseas obtener.

1. **Resumen**: Los gráficos dinámicos resumen grandes cantidades de datos y pueden mostrar totales, promedios, cuentas u otras estadísticas resumidas.

1. **Filtrado**: Ofrecen capacidades de filtrado, permitiendo mostrar solo los datos que cumplen ciertos criterios.

<br>
Los gráficos dinámicos se usan comúnmente en inteligencia empresarial y análisis de datos para ofrecer un resumen visual claro y conciso de conjuntos de datos complejos. Son una herramienta poderosa para tomar decisiones basadas en datos.

## Cómo agregar un PivotChart usando Aspose.Cells

### **Añadiendo una tabla dinámica**

Para crear una tabla dinámica usando Aspose.Cells:

1. Agrega algunos datos a las celdas de una hoja de cálculo usando el método `PutValue` o `SetValue` del objeto `Cell`. También puedes usar un archivo plantilla ya llenado con datos. Los datos se usarán como fuente de datos de la tabla dinámica.
1. Agrega una tabla dinámica a la hoja llamando al método `Add` de la colección `PivotTables` (encapsulada en el objeto `Worksheet`).
1. Accede al nuevo objeto `PivotTable` desde la colección `PivotTables` pasando su índice. Usa cualquiera de los objetos de tabla dinámica encapsulados en el objeto `PivotTable` para gestionar la tabla.

A continuación se muestran ejemplos de código.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PivotChart.go" >}}
### **Añadiendo un gráfico dinámico**

Para crear un gráfico dinámico usando Aspose.Cells:

1. Agregue un gráfico.
1. Establece el `PivotSource` del gráfico para hacer referencia a una tabla dinámica existente en la hoja de cálculo.
1. Establezca otros atributos.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PivotChart-1.go" >}}
