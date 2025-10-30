---
title: Obtener la hoja de cálculo del gráfico con Golang mediante C++
linktitle: Obtener hoja de cálculo del gráfico
description: Aprende cómo recuperar la hoja de cálculo asociada a un gráfico de Excel usando Aspose.Cells for C++. Nuestra guía te mostrará cómo acceder a la hoja y realizar operaciones sobre ella para manipular los datos subyacentes del gráfico.
keywords: Aspose.Cells for C++, gráficos de Excel, hojas de cálculo, manipulación de datos, datos subyacentes, operaciones.
type: docs
weight: 1000
url: /es/go-cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

A veces, quieres acceder a una hoja de cálculo desde una referencia de gráfico. Aspose.Cells proporciona el método [**Chart::GetWorksheet**](https://reference.aspose.com/cells/go-cpp/chart/getworksheet/) que devuelve la referencia de la hoja que contiene el gráfico.

{{% /alert %}}

 El siguiente ejemplo muestra cómo usar el método [**Chart::GetWorksheet**](https://reference.aspose.com/cells/go-cpp/chart/getworksheet/). El código primero imprime el nombre de la hoja, luego accede al primer gráfico en la hoja. Luego imprime nuevamente el nombre de la hoja, usando el método [**Chart::GetWorksheet**](https://reference.aspose.com/cells/go-cpp/chart/getworksheet/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetWorksheetOfTheChart.go" >}}
A continuación se muestra la salida de la consola que produce el código de ejemplo. Como puedes ver, imprime el mismo nombre de hoja de cálculo ambas veces.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
