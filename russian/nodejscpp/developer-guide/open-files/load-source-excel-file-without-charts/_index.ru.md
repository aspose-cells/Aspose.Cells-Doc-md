---
title: Загрузка исходного файла Excel без диаграмм с помощью Node.js через C++
linktitle: Загрузить исходный файл Excel без диаграмм
type: docs
weight: 420
url: /ru/nodejs-cpp/load-source-excel-file-without-charts/
description: Узнайте, как загрузить файл Excel без диаграмм, используя Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Aspose.Cells позволяет загружать ваши файлы Excel без диаграмм. Используйте свойство [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) для этого.

{{% /alert %}}

## **Загрузить электронную таблицу без диаграмм**

Следующий пример кода загружает пример файла Excel без диаграмм и сохраняет его в формате PDF.

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
{{< app/cells/assistant language="nodejs-cpp" >}}
