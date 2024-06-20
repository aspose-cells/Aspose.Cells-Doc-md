---
title: Obtener hoja de cálculo del gráfico
type: docs
weight: 80
url: /es/java/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

A veces, quieres acceder a una hoja de cálculo desde una referencia de un gráfico. Aspose.Cells proporciona la propiedad [**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet) que devuelve la referencia de la hoja de cálculo que contiene el gráfico.

{{% /alert %}}

## Ejemplo

El siguiente ejemplo muestra cómo usar la propiedad [**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet). El código primero imprime el nombre de la hoja de cálculo, luego accede al primer gráfico en la hoja de cálculo. Luego imprime nuevamente el nombre de la hoja de cálculo, usando la propiedad [**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet).

### Código Java para acceder a la hoja de trabajo del gráfico

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetWorksheetOfChart-GetWorksheetOfChart.java" >}}

### Salida de consola generada por el código de ejemplo

A continuación se muestra la salida de consola que genera el código de ejemplo. Como puedes ver, imprime el mismo nombre de la hoja de trabajo ambas veces.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
