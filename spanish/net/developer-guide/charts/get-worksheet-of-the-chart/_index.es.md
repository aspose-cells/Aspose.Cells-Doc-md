---
title: Obtener hoja de cálculo del gráfico
description: Aprende cómo recuperar la hoja de cálculo asociada a un gráfico de Excel usando Aspose.Cells for .NET. Nuestra guía te mostrará cómo acceder a la hoja de cálculo y realizar operaciones en ella para manipular los datos subyacentes del gráfico.
keywords: Aspose.Cells for .NET, gráficos de Excel, hojas de cálculo, manipulación de datos, datos subyacentes, operaciones.
type: docs
weight: 1000
url: /es/net/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

A veces, quieres acceder a una hoja de cálculo desde una referencia de un gráfico. Aspose.Cells proporciona la propiedad [**Chart.Worksheet**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/worksheet) que devuelve la referencia de la hoja de cálculo que contiene el gráfico.

{{% /alert %}}

El siguiente ejemplo muestra cómo usar la propiedad [**Chart.Worksheet**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/worksheet). El código primero imprime el nombre de la hoja de cálculo, luego accede al primer gráfico en la hoja de cálculo. Luego imprime nuevamente el nombre de la hoja de cálculo, usando la propiedad [**Chart.Worksheet**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/worksheet).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GetWorksheetOfTheChart-GetWorksheetOfTheChart.cs" >}}

A continuación se muestra la salida de la consola que produce el código de ejemplo. Como puedes ver, imprime el mismo nombre de hoja de cálculo ambas veces.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
