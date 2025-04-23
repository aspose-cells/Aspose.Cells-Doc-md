---
title: Obtener hoja de cálculo del gráfico
description: Aprende cómo recuperar la hoja de cálculo asociada a un gráfico de Excel usando Aspose.Cells para Python via .NET. Nuestra guía te mostrará cómo acceder a la hoja y realizar operaciones en ella para manipular los datos subyacentes del gráfico.
keywords: Aspose.Cells para Python via .NET, gráficos de Excel, hojas de cálculo, manipulación de datos, datos subyacentes, operaciones.
type: docs
weight: 1000
url: /es/python-net/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

A veces, quieres acceder a una hoja mediante la referencia de un gráfico. Aspose.Cells para Python via .NET proporciona la propiedad [**Chart.worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/worksheet) que devuelve la referencia de la hoja que contiene el gráfico.

{{% /alert %}}

El siguiente ejemplo muestra cómo usar la propiedad [**Chart.worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/worksheet). El código primero imprime el nombre de la hoja de cálculo, luego accede al primer gráfico en la hoja de cálculo. Luego imprime nuevamente el nombre de la hoja de cálculo, usando la propiedad [**Chart.worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/worksheet).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-GetWorksheetOfTheChart.py" >}}

A continuación se muestra la salida de la consola que produce el código de ejemplo. Como puedes ver, imprime el mismo nombre de hoja de cálculo ambas veces.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
