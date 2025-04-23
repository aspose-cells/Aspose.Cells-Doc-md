---
title: Cargar archivo de origen sin gráficos con Node.js vía C++
linktitle: Cargar archivo de Excel de origen sin gráficos
type: docs
weight: 420
url: /es/nodejs-cpp/load-source-excel-file-without-charts/
description: Aprenda cómo cargar un archivo de Excel sin gráficos usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Aspose.Cells le permite cargar su archivo de Excel sin gráficos. Por favor, utilice la propiedad [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) para este fin.

{{% /alert %}}

## **Cargar hojas de cálculo específicas en un libro de Excel**

El siguiente código de ejemplo carga el archivo de Excel de muestra sin gráficos y lo guarda en formato PDF de salida.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the load options and filter the data
const options = new AsposeCells.LoadOptions();

// Include everything except charts
options.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Chart));

// Load the workbook with specified load options
const workbook = new AsposeCells.Workbook(path.join(dataDir, "chart.xlsx"), options);

// Save the workbook in PDF format
workbook.save(path.join(dataDir, "ResultWithoutChart.pdf"), AsposeCells.SaveFormat.Pdf);
```
