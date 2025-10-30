---
title: Obtener la hoja de cálculo del gráfico con Node.js via C++
linktitle: Obtener hoja de cálculo del gráfico
description: Aprende cómo recuperar la hoja de cálculo asociada a un gráfico de Excel usando Aspose.Cells for Node.js via C++. Accede y manipula los datos subyacentes del gráfico de manera eficiente.
keywords: Aspose.Cells para Node.js, gráficos de Excel, hojas de cálculo, manipulación de datos, datos subyacentes, operaciones, Node.js vía C++
type: docs
weight: 1000
url: /es/nodejs-cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

A veces, quieres acceder a una hoja de cálculo desde una referencia de un gráfico. Aspose.Cells proporciona la propiedad [**Chart.getWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getWorksheet--) que devuelve la referencia de la hoja de cálculo que contiene el gráfico.

{{% /alert %}}

El siguiente ejemplo muestra cómo usar la propiedad [**Chart.getWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getWorksheet--). El código primero imprime el nombre de la hoja, luego accede al primer gráfico en la hoja. Después, imprime nuevamente el nombre de la hoja, usando la propiedad [**Chart.getWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getWorksheet--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Access first worksheet of the workbook
const worksheet = workbook.getWorksheets().get(0);

// Print worksheet name
console.log("Sheet Name: " + worksheet.getName());

// Access the first chart inside this worksheet
const charts = worksheet.getCharts();
if (charts.getCount() > 0) {
const chart = charts.get(0);

// Access the chart's sheet and display its name again
console.log("Chart's Sheet Name: " + chart.getWorksheet().getName());
} else {
console.log("No charts available in the worksheet.");
}
```

A continuación se muestra la salida de la consola que produce el código de ejemplo. Como puedes ver, imprime el mismo nombre de hoja de cálculo ambas veces.

{{< highlight javascript >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
